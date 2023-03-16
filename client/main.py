import time
import json
import tweepy

import get_tweet
import make_screenshot
import format_json

from config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    BEARER_TOKEN,
    USERNAME_BOT,
    USERID_BOT,
)

expansions = [
    "author_id",
    "referenced_tweets.id",
    "edit_history_tweet_ids",
    "in_reply_to_user_id",
    "referenced_tweets.id.author_id",
]
tweet_fields = [
    "attachments",
    "author_id",
    "created_at",
    "entities",
    "id",
    "public_metrics",
    "referenced_tweets",
    "source",
    "text",
]
user_fields = ["id", "name", "username", "verified", "profile_image_url"]


# usar el api v1 para poder responder con imagenes
auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)


# cliente para v2
client = tweepy.Client(
    BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)


class ListenerV2(tweepy.StreamingClient):
    """Streaming con la versión 2 del api de twitter"""

    def on_data(self, raw_data):

        time.sleep(5)

        # convertir a dict la raw_data
        data = json.loads(raw_data.decode()).get("data")

        # datos del tweet
        author_id = int(data.get("author_id"))
        tweet_id = data.get("id")
        text = data.get("text")
        referenced_tweets = data.get("referenced_tweets")

        if referenced_tweets is not None:

            type = data.get("referenced_tweets")[0].get("type")

            # filtro para responder
            if type == "replied_to" and f"@{USERNAME_BOT} cap" in text:

                # username del autor del tweet
                username = client.get_user(id=author_id).data.username

                # obtener lista de seguidores
                bot_followers = client.get_users_followers(id=USERID_BOT).data

                list_followers = [int(user.id) for user in bot_followers]

                # comprobar que sea un seguidor o que sea el mismo bot
                if author_id in list_followers or author_id == USERID_BOT:

                    # id del tweet al que hay que hacerle el sreenshot
                    in_reply_to = data.get("referenced_tweets")[0].get("id")

                    get_tweet.create_data(in_reply_to)
                    format_json.start()

                    if "cap" in text and "dark" in text:
                        make_screenshot.dark()

                    elif "cap" in text and "dark" not in text:
                        make_screenshot.default()

                    api.update_status_with_media(
                        status=f"@{username} 😎 Aquí tienes",
                        filename="screenshot.png",
                        in_reply_to_status_id=tweet_id,
                    )

                # si no es un seguidor
                else:

                    api.update_status(
                        status=f"@{username} 😎 sígueme para crear la captura.",
                        in_reply_to_status_id=tweet_id,
                        auto_populate_reply_metadata=True,
                    )



stream = ListenerV2(BEARER_TOKEN)

previous_rules = stream.get_rules().data

# eliminar reglas anteriores
if previous_rules:
    stream.delete_rules(previous_rules)


stream.add_rules(
    add=[
        tweepy.StreamRule(f"@{USERNAME_BOT} cap"),
        tweepy.StreamRule(f"@{USERNAME_BOT} cap dark"),
    ]
)



# ciclo while para reiniciar el stream luego de 10 segundos
# en caso de ocurrir algún error 
while True :
    
    print("runing..")
    
    try :

        stream.filter(
            expansions=expansions,
            user_fields=user_fields,
            tweet_fields=tweet_fields,
        )
    
    except Exception as error :

        print(error)

        stream.disconnect()
        time.sleep(20)
        
        continue


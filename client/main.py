from time import sleep
import get_tweet
import make_screenshot
import format_json
import tweepy

from config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    USERNAME_BOT,
)


auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)


class Listener(tweepy.Stream):
    def on_status(self, status):

        r = status.__dict__

        user_id = r["_json"]["user"]["id"]
        username = r["_json"]["user"]["screen_name"]
        reply_to = r["_json"]["id"]
        text = r["_json"]["text"]

        if (
            user_id in api.get_follower_ids(screen_name=USERNAME_BOT)
            or username == USERNAME_BOT
        ):

            in_reply_to_status_id = r["_json"]["in_reply_to_status_id_str"]

            if in_reply_to_status_id is not None:

                # obtener los datos del tweet

                get_tweet.create_data(in_reply_to_status_id)

                # formatear

                format_json.start()

                # hacer screenshot

                if f"@{USERNAME_BOT} cap dark" in text:
                    make_screenshot.black()

                elif f"@{USERNAME_BOT} cap" in text:
                    make_screenshot.default()

                # enviar screenshot
                text = f"@{username} 😎 Aquí tienes"

                api.update_status_with_media(
                    status=text,
                    filename="screenshot.png",
                    in_reply_to_status_id=reply_to,
                )

        else:

            text = f"@{username} 😎 sígueme para poder ayudarte a crear la captura."

            api.update_status(
                status=text,
                in_reply_to_status_id=reply_to,
                auto_populate_reply_metadata=True,
            )
        # para no sobrepasar el límite de solicitudes
        sleep(30)


stream = Listener(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream.filter(track=[f"@{USERNAME_BOT} cap", f"@{USERNAME_BOT} cap dark"])

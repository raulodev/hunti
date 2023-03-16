import requests
import json

from config import BEARER_TOKEN


def create_url(id: str):

    expansions = "expansions=attachments.media_keys,referenced_tweets.id,author_id,entities.mentions.username,attachments.poll_ids"

    media_fields = "media.fields=url,preview_image_url,width,height,alt_text,media_key"

    poll_fields = "poll.fields=id,options,voting_status"

    tweet_fields = "tweet.fields=attachments,author_id,created_at,entities,id,public_metrics,referenced_tweets,source,text"

    user_fields = "user.fields=id,name,username,verified,profile_image_url"

    ids = f"ids={id}"

    url = "https://api.twitter.com/2/tweets?{}&{}&{}&{}&{}&{}".format(
        ids, tweet_fields, expansions, user_fields, media_fields, poll_fields
    )

    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

    return response.json()


def create_embedded_data(id: str):
    """obtiene toda la información necesaria del tweet y luego
    la guarda en un archivo en formato json
    """
    url = create_url(id)
    json_response = connect_to_endpoint(url)
    data = json.dumps(json_response, indent=4, sort_keys=True)

    with open("./data/tweet_embedded.json", "w") as f:
        f.write(data)


def create_data(id: str):
    """obtiene toda la información necesaria del tweet y luego
    la guarda en un archivo en formato json
    """
    url = create_url(id)
    json_response = connect_to_endpoint(url)
    data = json.dumps(json_response, indent=4, sort_keys=True)

    with open("./data/tweet.json", "w") as f:
        f.write(data)

    try:
        tweet_id = json_response.get("includes")["tweets"][0]["id"]
        create_embedded_data(tweet_id)
    except Exception as err:
        pass

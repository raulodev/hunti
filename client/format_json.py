import json

tweets = []


def is_embedded():
    """verifica si el tweet referenciado es citado o solo es una respuesta"""
    
    file = open("./data/tweet.json", "r")
    r = json.JSONDecoder().decode(file.read())

    try:

        data = r.get("data")[0]["referenced_tweets"][0]["type"]

        if data == "quoted":

            return True, True

        return False, True

    except KeyError:

        return False, False


def format_data(filename: str, quoted: bool):
    """Formatea los datos para renderizar en la vista"""
    
    global tweets
    data = {}

    file = open(f"./data/{filename}.json", "r")
    r = json.JSONDecoder().decode(file.read())

    name = r.get("includes")["users"][0]["name"]
    username = r.get("includes")["users"][0]["username"]
    profile_image_url = r.get("includes")["users"][0]["profile_image_url"].replace(
        "_normal", ""
    )
    verified = r.get("includes")["users"][0]["verified"]
    created_at = r.get("data")[0]["created_at"]

    # text
    text = r.get("data")[0].get("text")
    if "http" in text[:4]:
        text = ""

    # media
    try:
        try:
            media = [m["url"] for m in r.get("includes")["media"]]
        except KeyError:
            media = [m["preview_image_url"] for m in r.get("includes")["media"]]
    except KeyError:
        media = []

    # poll
    try:
        poll_data = r.get("includes")["polls"][0]["options"]
        votes = [v["votes"] for v in poll_data]
        label = [v["label"] for v in poll_data]

        poll = []
        for index, vote in enumerate(votes):
            if vote == max(votes):
                first = True
            else:
                first = False

            poll.append({"text": label[index], "votes": vote, "first": first})

    except KeyError:
        poll = []

    # web
    try:
        web_image = r.get("data")[0]["entities"]["urls"][0]["images"][0]["url"]
    except KeyError:
        web_image = ""

    try:
        web_domain = r.get("data")[0]["entities"]["urls"][0]["expanded_url"]
    except KeyError:
        web_domain = ""

    try:
        web_title = r.get("data")[0]["entities"]["urls"][0]["title"]
    except KeyError:
        web_title = ""

    try:
        web_description = r.get("data")[0]["entities"]["urls"][0]["description"]
    except KeyError:
        web_description = ""

    if web_description == web_image == web_title == web_image:
        web = {}

    else:

        web = {
            "image": web_image,
            "domain": web_domain,
            "title": web_title,
            "description": web_description,
        }

    data["name"] = name
    data["username"] = username
    data["user_is_verified"] = verified
    data["profile_photo"] = profile_image_url
    data["created"] = created_at
    data["text"] = text
    data["media"] = media
    data["poll"] = poll
    data["web"] = web

    if quoted:

        tweets[0]["embedded"] = data
    else:
        tweets.insert(0, data)


def start():

    global tweets

    quoted, exist = is_embedded()
    format_data(filename="tweet", quoted=False)
    # solo si existe un tweet citado o respondido
    # se ejecutará esta función
    if exist:
        format_data(filename="tweet_embedded", quoted=quoted)

    data = json.dumps(tweets, indent=4)
    # guardar datos
    with open("../data/data.json", "w") as f:
        f.write(data)
    # reiniciar valores
    tweets = []

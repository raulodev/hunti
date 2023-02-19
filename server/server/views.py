import json
from django.shortcuts import render


def default(request):

    # content = read_json_test()
    content = read_json()
    return render(request, "default.html", context={"data": content})


def black(request):

    # content = read_json_test()
    content = read_json()
    return render(request, "black.html", context={"data": content})


def read_json():

    file = open("../data/data.json", "r")
    r = json.JSONDecoder().decode(file.read())

    return r


def read_json_test():

    content = []

    only_text = {
        "name": "Raul Cobiellas",
        "username": "raulodev_",
        "user_is_verified": True,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "#Rapidiously actualize @error-freeodologies. Uniquely restore enterprise expertise via.",
        "media": [],
        "poll": [],
        "web": {},
        "embedded": {
            "name": "",
            "username": "",
            "user_is_verified": False,
            "profile_photo": "",
            "created": "",
            "text": "",
            "media": [],
            "poll": [],
            "web": {},
        },
    }

    only_media = {
        "name": "Raul Cobiellas",
        "username": "raulodev_",
        "user_is_verified": True,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "",
        "media": [1, 2, 3],
        "poll": [],
        "web": {},
        "embedded": {
            "name": "",
            "username": "",
            "user_is_verified": False,
            "profile_photo": "",
            "created": "",
            "text": "",
            "media": [],
            "poll": [],
            "web": {},
        },
    }

    only_poll = {
        "name": "Raul Cobiellas",
        "username": "raulodev_",
        "user_is_verified": True,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "",
        "media": [],
        "poll": [
            {"text": "opcion1", "votes": 0, "first": False},
            {"text": "opcion2", "votes": 50, "first": True},
            {"text": "opcion2", "votes": 25, "first": False},
        ],
        "web": {},
        "embedded": {
            "name": "",
            "username": "",
            "user_is_verified": False,
            "profile_photo": "",
            "created": "",
            "text": "",
            "media": [],
            "poll": [],
            "web": {},
        },
    }

    only_web = {
        "name": "Raul Cobiellas",
        "username": "raulodev_",
        "user_is_verified": True,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "",
        "media": [],
        "poll": [],
        "web": {
            "image": "image.png",
            "domain": "https://twitter.com/elonmusk/status/1625696554467344384/photo/1",
            "title": "Avanzar para adelante",
            "description": "Conveniently network customized outsourcing via user friendly e-commerce. Rapidiously generate.",
        },
        "embedded": {
            "name": "",
            "username": "",
            "user_is_verified": False,
            "profile_photo": "",
            "created": "",
            "text": "",
            "media": [],
            "poll": [],
            "web": {},
        },
    }

    # tweets embeddeds
    only_ti_text = {
        "name": "Raul Cobiellas",
        "username": "raulodev_",
        "user_is_verified": True,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "",
        "media": [],
        "poll": [],
        "web": {},
        "embedded": {
            "name": "brun",
            "username": "username",
            "user_is_verified": True,
            "profile_photo": "user.jpg",
            "created": "2023-01-14T21:00:07.000Z",
            "text": "Assertively communicate extensive content with multimedia #based.",
            "media": [],
            "poll": [],
            "web": {},
        },
    }

    only_ti_media = {
        "name": "Raul Cobiellas",
        "username": "raulodev_",
        "user_is_verified": True,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "",
        "media": [],
        "poll": [],
        "web": {},
        "embedded": {
            "name": "brun",
            "username": "username",
            "user_is_verified": True,
            "profile_photo": "user.jpg",
            "created": "2023-01-14T21:00:07.000Z",
            "text": "",
            "media": [1, 2, 3],
            "poll": [],
            "web": {},
        },
    }

    only_ti_poll = {
        "name": "Raul Cobiellas",
        "username": "raulodev_",
        "user_is_verified": True,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "",
        "media": [],
        "poll": [],
        "web": {},
        "embedded": {
            "name": "brun",
            "username": "username",
            "user_is_verified": True,
            "profile_photo": "user.jpg",
            "created": "2023-01-14T21:00:07.000Z",
            "text": "",
            "media": [],
            "poll": [
                {"text": "opcion1", "votes": 0, "first": False},
                {"text": "opcion2", "votes": 50, "first": True},
                {"text": "opcion2", "votes": 0, "first": False},
            ],
            "web": {},
        },
    }

    only_ti_web = {
        "name": "Raul Cobiellas",
        "username": "raulodev_",
        "user_is_verified": True,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "",
        "media": [],
        "poll": [],
        "web": {},
        "embedded": {
            "name": "brun",
            "username": "username",
            "user_is_verified": True,
            "profile_photo": "user.jpg",
            "created": "2023-01-14T21:00:07.000Z",
            "text": "",
            "media": [],
            "poll": [],
            "web": {
                "image": "image.png",
                "domain": "https://twitter.com/elonmusk/status/1625696554467344384/photo/1",
                "title": "Avanzar para adelante",
                "description": "Conveniently network customized outsourcing via user friendly e-commerce. Rapidiously generate.",
            },
        },
    }

    tweet_1 = {
        "name": "Raul Cobiellas",
        "username": "raulodev_",
        "user_is_verified": True,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "#Rapidiously actualize @error-freeodologies. Uniquely restore enterprise expertise via.",
        "media": [],
        "poll": [
            {"text": "opcion1", "votes": 2},
            {"text": "opcion2", "votes": 50},
            {"text": "opcion2", "votes": 25},
        ],
        "web": {},
        "embedded": {
            "name": "name INRUSTADO",
            "username": "jorg4 embedded",
            "user_is_verified": False,
            "profile_photo": "user.jpg",
            "created": "2023-01-14T21:00:07.000Z",
            "web": {
                "image": "image.png",
                "domain": "wwww.example.com",
                "title": "Avanzar para adelante",
                "description": "Conveniently network customized outsourcing via user friendly e-commerce. Rapidiously generate.",
            },
        },
    }
    tweet_2 = {
        "name": "many",
        "username": "jorg4",
        "user_is_verified": False,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "@Rapidiously architect an \n \n #expanded array of expertise for world-class materials.",
        "media": [],
        "poll": [],
        "web": {
            "image": "image.png",
            "domain": "wwww.example.com",
            "title": "Avanzar para adelante",
            "description": "Conveniently network customized outsourcing via user friendly e-commerce. Rapidiously generate.",
        },
        "embedded": {},
    }
    tweet_3 = {
        "name": "many",
        "username": "jorg4",
        "user_is_verified": False,
        "profile_photo": "user.jpg",
        "created": "2023-01-14T21:00:07.000Z",
        "text": "@Rapidiously architect 😂😂 an \n \n #expanded array of expertise for world-class materials.",
        "media": [],
        "poll": [],
        "web": {},
        "embedded": {
            "name": "name INRUSTADO",
            "username": "jorg4 embedded",
            "user_is_verified": False,
            "profile_photo": "user.jpg",
            "created": "2023-01-14T21:00:07.000Z",
            "text": " #expanded array",
            "media": [],
            "poll": [
                {"text": "opcion1", "votes": 5},
                {"text": "opcion2", "votes": 50},
                {"text": "opcion2", "votes": 25},
            ],
            "web": {},
        },
    }

    # content.append(only_text)
    # content.append(only_media)
    content.append(only_web)
    # content.append(tweet_1)
    # content.append(only_poll)
    # content.append(only_ti_text)
    # content.append(only_ti_media)
    # content.append(only_ti_poll)
    content.append(only_ti_web)

    return content

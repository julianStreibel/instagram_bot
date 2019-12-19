#!/usr/bin/env python
# coding: utf8

import time
import random
from insta_bot import InstagramBot

if __name__ == "__main__":

    username = "justcats2dogs"
    password = "TESTtest1997"
    hashtags = [
        "beautiful",
        "adventure",
        "photography",
        "lion",
        "cinematography",
        "pretty",
        "pets",
        "animal",
        "pet",
        "cute",
        "dogs",
        "nature",
        "dog",
        "petstagram",
        "cats",
        "puppy",
        "photooftheday",
        "cat",
        "adorable",
        "petsagram",
        "dogsofinstagram",
        "doglover",
        "wildlife",
        "dogstagram",
        "instadog",
        "kittens",
        "dogoftheday",
        "ilovemydog",
        "animallovers",
        "instapuppy",
        "instagramdogs",
        "kitten",
        "puppies",
        "catsofinstagram",
        "nature",
        "animals",
        "animal",
        "wildlifephotography",
        "wild",
        "photography",
        "bird",
        "travel",
        "explore",
        "conservation",
        "outdoors",
        "africa",
        "forest",
        "lion",
        "natgeo",
        "landscape",
        "photooftheday",
        "earth",
        "naturephotography",
        "world",
        "birds",
        "mountain",
        "wildlifeplanet",
        "picoftheday",
    ]

    comments = [
        "pretty nice!!",
        "good content",
        "Thats nice!",
        "Wow :D",
        "Nice :)",
        "I like your stuff!",
        "Nice one!",
        "haha nice!",
    ]

    pages = [
        "animalsinfluence",
        "animals.co",
        "animalsvideos",
        "lovinganimals.dg",
        "babyanimalshq",
        "discover.animal",
        "animalsshot",
        "wildviewing",
    ]

    ig = InstagramBot(username, password, "chrome")
    ig.login()

    while True:
        try:  # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            page = random.choice(pages)
            # ig.attack_hashtag(tag, comments, 1, True, True)
            # ig.unfollow()
            ig.attack_page(page, 500, 2)
            # ig.attack_comments_of_page(page, 2, False, 3)

        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password, "chrome")
            ig.login()
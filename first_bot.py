#!/usr/bin/env python
# coding: utf8

import time
import random
from insta_bot import InstagramBot

if __name__ == "__main__":

    username = ""  # your username
    password = ""  # your password
    hashtags = [
        "followtofollow",
        "follow4followback",
        "followforfollowback",
        "followfllow",
        "follow4like",
        "following",
        "follow",
        "followers",
        "followmeto",
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
        try:
            tag = random.choice(hashtags)
            page = random.choice(pages)
            # ig.attack_page(page, 500, 2)
            # ig.unfollow()
            ig.attack_comments_of_page(page, 2, True, 3)

        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password, "chrome")
            ig.login()

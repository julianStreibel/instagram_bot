#!/usr/bin/env python
# coding: utf8

import time
import random
from insta_bot import InstagramBot

if __name__ == "__main__":

    username = "justhighasf"
    password = "TESTtest1997"
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
        "weed",
        "weed._planet",
        "weed.enjoy",
        "weedbros.inc",
        "the.weed.blog",
        "420welcome",
        "vidadelcanna",
        "mavglass",
        "highpeopledoingstuff",
        "herbsaver",
        "southerndabber_420",
        "the_cannabis_squirrel",
        "phonehomie",
        "cannabis_now_",
        "official_weed_time_",
        "weedwooks",
    ]

    ig = InstagramBot(username, password, "chrome")
    ig.login()

    while True:
        try:  # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            page = random.choice(pages)
            # ig.attack_page("weed._planet", 500, 2)
            # ig.unfollow()
            ig.attack_comments_of_page(page, 2, True, 3)

        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password, "chrome")
            ig.login()
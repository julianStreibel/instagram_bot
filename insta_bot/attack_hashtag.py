#!/usr/bin/env python
# coding: utf8

import time
import random
from helpers import (
    visit_hashtag,
    colect_links_from_stream,
    visit_post,
    like_post_from_post,
    sub_from_post,
    comment_post,
    visit_author_from_post,
    like_posts_from_account,
)


def attack_hashtag(driver, hashtag, comments, likes, follow, comment):
    # go to hashtag
    visit_hashtag(hashtag, driver)
    # gathering photos
    try:
        pic_hrefs = colect_links_from_stream(5, driver)
    except Exception as e:
        pic_hrefs = []
        print(e)
    # Liking photos and following
    unique_photos = len(pic_hrefs)
    for pic_href in pic_hrefs:
        # go to post
        visit_post(driver, pic_href)
        try:
            time.sleep(random.randint(2, 4))

            # Like
            if likes > 0:
                try:
                    like_post_from_post(driver)
                except Exception as e:
                    print("failed at liking first post")
                    print(e)

            # Subscribe
            if follow:
                try:
                    sub_from_post(driver)
                except Exception as e:
                    print("failed at following")
                    print(e)

            if comment and random.randint(0, 40) < 500:
                try:
                    # comment
                    comment_post(driver, comments)
                except Exception as e:
                    print("failed at commenting post")
                    print(e)

            if likes > 1:
                try:
                    # Go to author
                    visit_author_from_post(driver)
                    # Like x posts of the author
                    like_posts_from_account(driver, likes - 1)
                except Exception as e:
                    print("failed at liking more posts")
                    print(e)

            # Sleep to dodge spam limits
            for second in reversed(range(0, random.randint(37, 45))):
                print(
                    "#"
                    + hashtag
                    + ": unique photos left: "
                    + str(unique_photos)
                    + " | Sleeping "
                    + str(second)
                )
                time.sleep(1)

        except Exception as e:
            time.sleep(2)
            print("fail at this post")
            print(e)
        unique_photos -= 1
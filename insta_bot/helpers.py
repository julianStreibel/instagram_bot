#!/usr/bin/env python
# coding: utf8

import time
import random

# likes the first n pics of the current account page
# driver: is on an accounts page
def like_posts_from_account(driver, n):
    try:
        pic_hrefs_author = colect_links_from_stream(n / 9 + 1, driver)
    except Exception as e:
        print(e)
        pic_hrefs_author = []
        time.sleep(random.randint(2, 4))
    # Like these n pictures
    for pic_href_author in pic_hrefs_author[0 : min(n, len(pic_hrefs_author))]:
        visit_post(driver, pic_href_author)
        try:
            time.sleep(random.randint(2, 4))
            # Like
            like_post_from_post(driver)
        except Exception as e:
            print(e)
            continue


# visits author of current post
# driver: driver has to be on a post
# time: E() = 3 sec
def visit_author_from_post(driver):
    author_button = lambda: driver.find_element_by_xpath(
        '//a[contains(@class,"nJAzx")]'
    )
    author_button().click()
    print("visit author")
    time.sleep(random.randint(2, 4))


# comments the current post
# driver: driver has to be on a post
# comment: is the commed that gets posted
# time: E() = 15 sec
def comment_post(driver, comments):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.randint(1, 2))
    comment = random.choice(comments)
    comment_elem = driver.find_element_by_xpath("//textarea[contains(@class, 'Ypffh')]")
    comment_elem.click()
    comment_elem = driver.find_element_by_xpath("//textarea[contains(@class, 'Ypffh')]")
    comment_elem.send_keys(comment)
    time.sleep(random.randint(2, 4))
    comment_button = lambda: driver.find_element_by_xpath(
        '//form[@class="X7cDz"]//button[@type="submit"]'
    )
    comment_button().click()
    print("comment: " + comment)
    time.sleep(random.randint(10, 15))


# subscribes to author of the current post
# driver: driver has to be on a post view
# time: E() = 3 sec
def sub_from_post(driver):
    driver.execute_script("window.scrollTo(0, 0);")
    subscribe_button = lambda: driver.find_element_by_xpath(
        '//div[@class="bY2yH"]//button[@type="button"]'
    )
    subscribe_button().click()
    print("subscribe author")
    time.sleep(random.randint(2, 4))


# likes the current post
# driver: driver has to be on a post view
# time: E() = 3 sec
def like_post_from_post(driver):
    like_button = lambda: driver.find_element_by_xpath(
        '//span[@aria-label="Gefällt mir"]'
    )
    like_button().click()
    print("like post")
    time.sleep(random.randint(2, 4))


# goes to post page and scrolls down
# driver: driver dont has to be by any specific page
# pic_href: is the link of the target post
# time: 2 sec
def visit_post(driver, pic_href):
    driver.get(pic_href)
    time.sleep(2)
    print("visit post")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# looks at current fotostream (eg hashtag page), scrolls *scrolls times and collects links of pictures
# scrolls: number of scrolls on page
# driver: driver that has to be on an fotostream
# returns: list of links to pictures
# time: scrolls * 2 sec
def colect_links_from_stream(scrolls, driver):
    pic_hrefs = []
    print("collect posts")
    for i in range(0, scrolls):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # get tags
            hrefs_in_view = driver.find_elements_by_tag_name("a")
            # finding relevant hrefs
            hrefs_in_view = [
                elem.get_attribute("href")
                for elem in hrefs_in_view
                if ".com/p/" in elem.get_attribute("href")
            ]
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
        except Exception as e:
            print(e)
            continue
    return pic_hrefs


# goes to hashtag fotostream
# hashtag: hashtag to goto
# driver: driver dont has to be by any specific page
# time: 2 sec
def visit_hashtag(hashtag, driver):
    driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    print("visit " + hashtag)
    time.sleep(2)


# looks at current subs , scrolls *scrolls times and collects links of acc that have subscribed
# scrolls: number of scrolls on page
# driver: driver that has to be on an fotostream
# returns: list of links to pictures
# time: scrolls * 2 sec
def colect_links_from_stream_in_element(scrolls, driver, scroll_element):
    pic_hrefs = []
    print("collect posts")
    for i in range(0, scrolls):
        try:
            if scroll_element:
                driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element
                )
            else:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randint(3, 5))
            # get tags
            hrefs_in_view = driver.find_elements_by_class_name("FPmhX")

            # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute("href") for elem in hrefs_in_view]

            print(hrefs_in_view)
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
        except Exception as e:
            print(e)
            continue

    return pic_hrefs


# looks at comments on a post-page , scrolls *scrolls times and collects links of acc that have commented
# scrolls: number of scrolls on page
# driver: driver that has to be on an fotostream
# returns: list of links to authors
# time: scrolls * 2 sec
def colect_authors_from_comments_on_post(scrolls, driver, scroll_element):
    pic_hrefs = []
    print("collect posts")
    for i in range(0, scrolls):
        try:
            # scroll down
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroll_element
            )
            time.sleep(random.randint(2, 3))
            # click more
            try:
                plus_element = driver.find_element_by_xpath(
                    "//div[contains(@class,'YBx95')]//button[contains(@class,'_0mzm-')]"
                )
            except Exception:
                plus_element = False

            if plus_element:
                plus_element.click()
                time.sleep(random.randint(2, 3))

            # get tags
            hrefs_in_view = driver.find_elements_by_class_name("FPmhX")

            # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute("href") for elem in hrefs_in_view]

            print(hrefs_in_view)
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
        except Exception as e:
            print(e)
            continue

    return pic_hrefs


# make_element: makes an dict with name and button
def make_element(elem):
    re = {}
    re["name"] = elem.find_element_by_tag_name("a").get_attribute("title")
    re["button"] = elem.find_element_by_tag_name("button")
    return re


# sub_from_account: subscribes an account from its page
# driver: has to be on the accounts page
def sub_from_account(driver):
    try:
        follow_button = driver.find_element_by_xpath(
            "//div[contains(@class,'nZSzR')]//button[contains(text(),'Folgen')]"
        )
    except Exception:
        follow_button = False
    if follow_button:
        follow_button.click()
        print("subscribed")
    time.sleep(random.randint(2, 4))
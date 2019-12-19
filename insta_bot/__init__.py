#!/usr/bin/env python
# coding: utf8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import math
from attack_page import attack_page as OGattack_page
from attack_hashtag import attack_hashtag as OGattack_hashtag
from attack_comments_of_page import attack_comments_of_page as OGattack_comments_of_page
from friendly_unfollow import friendly_unfollow as OGfriendly_unfollow
from unfollow import unfollow as OGunfollow


class InstagramBot:

    # Constructor
    # username: of instagram acc
    # password: of insagram acc
    # browser: ("chrome" | "firefox") in which the bot works has to be diffrent in every bot on one machine
    def __init__(self, username, password, browser):
        self.username = username
        self.password = password
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            self.driver = webdriver.Firefox()

    # Closes the Browser
    def closeBrowser(self):
        self.driver.close()

    # Open Instagram and login
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']"
        )
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath(
            "//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        print("logged into " + self.username)
        time.sleep(7)

    # Goes through the hashtag, follows people and likes theire pictures
    # hashtag: string;
    # comments: string[];
    # likes: number; of likes per person
    # follow: boolean;
    # comment: boolean;
    def attack_hashtag(self, hashtag, comments, likes, follow, comment):
        OGattack_hashtag(self.driver, hashtag, comments,
                         likes, follow, comment)

    # Follow subscriber of an page, and like their pictures
    # page: page with good subscribers
    # max_follow: max people to follow
    # likes: how much likes per subscriber
    def attack_page(self, page, max_follow, likes):
        OGattack_page(self.driver, page, max_follow, likes)

    # Goes through comments of page and attacks the author
    # page: page with comments
    # like: number of likes per author
    # follow: author of comment
    # n: attack n posts of page
    def attack_comments_of_page(self, page, like, follow, n):
        OGattack_comments_of_page(self.driver, page, like, follow, n)

    # Unfollows all followers of the page
    def unfollow(self):
        OGunfollow(self.driver, self.username)

    # Unfollows every acc that dosnt follows back         <--- TODO: not done jet
    def friendly_unfollow(self):
        OGfriendly_unfollow(self.driver, self.username)

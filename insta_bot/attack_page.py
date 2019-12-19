import time
import random
from helpers import like_posts_from_account, sub_from_account

# Looks at follower of a page and likes and follows the followers of them
# page: name of the page
# max_follow: max number of follows per page
# likes: number of likes per follower
# time: E(t) =? 17
def attack_page(driver, page, max_follow, likes):
    # go to page
    driver.get("https://www.instagram.com/" + page)
    time.sleep(random.randint(2, 3))
    # open follower
    subs_button = lambda: driver.find_element_by_xpath(
        "//a[contains(@href,'followers')]"
    )
    subs_button().click()
    time.sleep(random.randint(1, 2))
    # scroll up
    scroll_element = driver.find_element_by_xpath("//div[contains(@class,'isgrP')]")
    for i in range(0, 5):
        driver.execute_script("arguments[0].scrollTop = 0", scroll_element)
        time.sleep(1)
    time.sleep(random.randint(1, 2))
    # scan max followers
    followers = []
    # scann followers
    while len(followers) < max_follow:
        try:
            time.sleep(random.randint(1, 2))
            # get tags
            titles_in_view = driver.find_element_by_xpath(
                "//div[contains(@class,'isgrP')]"
            ).find_elements_by_tag_name("a")
            # finding name
            titles_in_view = [elem.get_attribute("title") for elem in titles_in_view]
            # building list of unique names
            [
                followers.append(title)
                for title in titles_in_view
                if title not in followers
            ]
            scroll_element = driver.find_element_by_xpath(
                "//div[contains(@class,'isgrP')]"
            )
            driver.execute_script(
                "arguments[0].scrollTo(0, 9999999999)", scroll_element
            )
        except Exception as e:
            print(e)
            continue
        print(len(followers))
    # go follow and like all in followers
    for name in followers:
        try:
            # go to name
            driver.get("https://www.instagram.com/" + name)
            time.sleep(random.randint(2, 3))
            # sub to name
            sub_from_account(driver)
            time.sleep(random.randint(4, 6))
            # like first likes posts
            like_posts_from_account(driver, likes)
        except Exception as e:
            print(e)
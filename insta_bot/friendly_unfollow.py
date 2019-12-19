import time
import random
from helpers import make_element, colect_links_from_stream_in_element

# Looks for acc that havent subscribed and unsubscribe them
def friendly_unfollow(driver, username):
    # go to my page
    driver.get("https://www.instagram.com/" + username)
    time.sleep(random.randint(2, 3))

    # open subs
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

    not_all = True
    followers = []
    last_sum = -1

    # scann followers
    while not_all:
        try:
            time.sleep(2)
            # get tags
            titles_in_view = driver.find_element_by_xpath(
                "//div[contains(@class,'isgrP')]"
            ).find_elements_by_tag_name("a")
            # finding relevant hrefs
            titles_in_view = [elem.get_attribute("title") for elem in titles_in_view]
            # building list of unique photos
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
        print(followers)
        print(len(followers))
        not_all = last_sum != len(followers)
        last_sum = len(followers)

    print("fertig mit followers")

    # scann following
    not_all = True
    following = []
    last_sum = -1

    # go to my page
    driver.get("https://www.instagram.com/" + username)
    time.sleep(random.randint(2, 3))

    # open subs
    subs_button = lambda: driver.find_element_by_xpath(
        "//a[contains(@href,'following')]"
    )
    subs_button().click()
    time.sleep(random.randint(1, 2))

    while not_all:
        try:
            time.sleep(2)
            # get elements
            elements_in_view = driver.find_elements_by_xpath(
                "//div[contains(@class,'uu6c_')]"
            )
            # make element dict
            elements_in_view = [
                make_element(elem)
                for elem in elements_in_view
                if elem.find_element_by_tag_name("a").get_attribute("title") != ""
            ]

            # building list of uniques
            [
                following.append(elem)
                for elem in elements_in_view
                if elem not in following
            ]

            # unfollow if not in follers
            for element in following:
                if element["name"] not in followers and "_8A5w5" in element[
                    "button"
                ].get_attribute("class"):
                    element["button"].click()
                    time.sleep(random.randint(2, 3))
                    unsub_button = driver.find_element_by_xpath(
                        '//button[contains(@class, "-Cab_")]'
                    )
                    unsub_button.click()
                    time.sleep(random.randint(15, 20))
            scroll_element = driver.find_element_by_xpath(
                "//div[contains(@class,'isgrP')]"
            )
            driver.execute_script(
                "arguments[0].scrollTo(0, 9999999999)", scroll_element
            )
        except Exception as e:
            print(e)
            continue
        print(following)
        print(len(following))
        not_all = last_sum != len(following)
        last_sum = len(following)

    print("fertig mit following")
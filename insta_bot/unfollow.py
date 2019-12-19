import time
import random
from helpers import make_element, colect_links_from_stream_in_element

# Looks for acc that havent subscribed and unsubscribe them
def unfollow(driver, username):
    # go to my page
    driver.get("https://www.instagram.com/" + username)
    time.sleep(random.randint(2, 3))

    # open subs
    subs_button = lambda: driver.find_element_by_xpath(
        "//a[contains(@href,'following')]"
    )
    subs_button().click()
    time.sleep(random.randint(1, 2))

    # are subscribed people left in view?
    in_view = lambda: len(
        driver.find_elements_by_xpath("//button[contains(text(),'Abonniert')]")
    )
    print("anzahl an abonnierten usern", in_view())

    while in_view() > 0:
        print("anzahl an abonnierten usern", in_view())
        try:
            time.sleep(random.randint(5, 25))
            driver.find_element_by_xpath(
                "//button[contains(text(),'Abonniert')]"
            ).click()
            time.sleep(random.randint(5, 25))
            driver.find_element_by_xpath(
                "//button[contains(text(),'Nicht mehr folgen')]"
            ).click()

        except Exception as e:
            print(e)
            print("fehler beim deabonnieren")
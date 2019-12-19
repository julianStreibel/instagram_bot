import time
import random

from helpers import (
    colect_links_from_stream,
    colect_authors_from_comments_on_post,
    like_posts_from_account,
    sub_from_account,
)

# attack_comments_of_page: goes in the comments of a page and likes the comment-owners conntnent
# driver: driver of the bot
# page: that gets attacked
# like: how much likes per comment-author
# follow: follow author of comment
# n: number of post from page that get attacked
def attack_comments_of_page(driver, page, like, follow, n):
    MIN_FOLLOWING_RATIO = 0.5  # = abonniert / Abonnenten
    # go to page
    driver.get("https://www.instagram.com/" + page)
    time.sleep(random.randint(2, 4))
    # build list of posts
    posts_on_page = colect_links_from_stream(2, driver)[0:n]
    time.sleep(random.randint(2, 4))
    # go to each post
    for href in posts_on_page:
        try:
            # go to post
            driver.get(href)
            time.sleep(random.randint(2, 4))
            # build list of author of comments
            scroll_element = driver.find_element_by_xpath(
                "//ul[contains(@class,'XQXOT')]"
            )

            author_links = colect_authors_from_comments_on_post(
                3, driver, scroll_element
            )

            # go to each author and like and subscribe
            random.shuffle(author_links)
            for author in author_links:
                try:
                    if author != "https://www.instagram.com/" + page + "/":
                        driver.get(author)
                        time.sleep(random.randint(2, 4))
                        # is following_ratio correct?
                        if ratio_is_correct(driver, MIN_FOLLOWING_RATIO):
                            if follow:
                                sub_from_account(driver)
                                time.sleep(random.randint(2, 4))
                            like_posts_from_account(driver, like)
                        else:
                            print("not good following ratio")
                except Exception as e:
                    print(e)
                    print("faild on author/ maybe following already")
                    continue

        except Exception as e:
            print(e)
            print("faild on attacking post", href)


# looks if (abonniert / Abonnenten > MIN_FOLLOWING_RATIO)
# driver:
# min: MIN_FOLLOWING_RATIO
def ratio_is_correct(driver, min):
    try:  # to look up
        try:
            abonnenten = float(
                driver.find_element_by_xpath(
                    "//a[contains(@href, 'follower')]//span"
                ).text.replace(".", "")
            )
            abonniert = float(
                driver.find_element_by_xpath(
                    "//a[contains(@href, 'following')]//span"
                ).text.replace(".", "")
            )
        except Exception:
            list = driver.find_elements_by_xpath("//span[contains(@class, 'g47SY')]")
            abonnenten = float(list[1].text.replace(".", ""))
            abonniert = float(list[2].text.replace(".", ""))
    except Exception as e:
        print(e)
        print("failed to locate followers or following")
        abonnenten = 10
        abonniert = 1
    if abonniert / abonnenten < min:
        return False
    return True
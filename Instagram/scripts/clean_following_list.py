from Instagram import instagram_actions as insta_actions
from General import db_all
from General import driver_browser
from General import Setting
from General import general_actions
from General import time_utility as time

driver = driver_browser.initialize_driver()
database = db_all.Database()
driver.get(Setting.instagram_link)
def add_unregisted_followers_to_database(number_users):
    insta_actions.go_to_profile(driver, Setting.my_profile_name)
    insta_actions.click_following_profile_page(driver)
    for i in range(400, number_users):
        popupbox = insta_actions.get_all_users_popup_list(driver)
        while (len(popupbox) - 1 < i):
            try:
                general_actions.scroll_to_element(driver, popupbox[len(popupbox)-1])
                popupbox = insta_actions.get_all_users_popup_list(driver)
            except Exception as e:
                print(e)
                continue;
        print("finish scrolling")
        insta_actions.click_username_popup_list(driver, popupbox[i])
        add_unregisted_follower_to_database()
        time.small_timeout()
        if(i % 10 == 0 ):
            database.commit()
        driver.back()


def add_unregisted_follower_to_database():
    username = insta_actions.get_username_profile_page(driver)
    post = insta_actions.get_number_posts_profile_page(driver)
    followers = insta_actions.get_number_followers_profile_page(driver)
    following = insta_actions.get_number_following_profile_page(driver)
    if(not database.find_instagram_user_by_name(username)):
        database.add_instagram_user(username=username, posts=post, followers=followers, following=following,
                                    isFollowing=False);
        insta_actions.click_unfollow_profile_page(driver)
add_unregisted_followers_to_database(2000)
driver.close()
database.connection.close()

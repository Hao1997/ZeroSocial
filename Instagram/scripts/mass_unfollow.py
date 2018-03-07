
from Instagram import instagram_actions as insta_actions
from General import db_all
from General import driver_browser
from General import Setting
from General import general_actions
from General import time_utility as time

driver = driver_browser.initialize_driver()
def mass_unfollow(number_users):
    insta_actions.go_to_profile(driver, Setting.my_profile_name)
    insta_actions.click_following_profile_page(driver)
    for i in range(0, number_users):
        popupbox = insta_actions.get_all_users_popup_list(driver)
        while (len(popupbox) - 1 < i):
            try:
                general_actions.scroll_to_element(driver, popupbox[len(popupbox) - 1])
                popupbox = insta_actions.get_all_users_popup_list(driver)
            except Exception as e:
                print(e)
                continue;
        print("finish scrolling")
        insta_actions.click_username_popup_list(driver, popupbox[i])
        insta_actions.click_unfollow_profile_page(driver)
        driver.back()
mass_unfollow(50)
driver.close()
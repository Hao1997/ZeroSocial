from General import time_utility as time
from General import numbers_util as fnum

def go_to_profile(driver, profilename):
    driver.get("https://www.instagram.com/" + profilename)
    time.big_timeout()

def search_bar_instagram(driver, text):
        # click on search box
        driver.find_element_by_class_name('_96n9j').click()
        # type search item
        driver.find_element_by_xpath(".//input[@class = '_avvq0 _o716c']").send_keys(text)
        time.medium_timeout();
        # click on first search item
        driver.find_elements_by_xpath(".//div[@class = '_etpgz']/a[@class = '_gimca']")[0].click()
        time.big_timeout()

#click from profile page
def click_followers_profile_page(driver):
    driver.find_elements_by_xpath(".//ul[@class = '_h9luf']/li")[1].click()
    time.big_timeout()

def click_following_profile_page(driver):
    driver.find_elements_by_xpath(".//ul[@class = '_h9luf']/li")[2].click()
    time.big_timeout()

def click_follow_profile_page(driver):
    if(not is_following_profile_page(driver)):
        driver.find_element_by_xpath(".//button[@class = '_qv64e _t78yp _r9b8f _njrw0']").click()
    time.medium_timeout()

def click_unfollow_profile_page(driver):
    if (is_following_profile_page(driver)):
        driver.find_element_by_xpath(".//button[@class = '_qv64e _t78yp _r9b8f _njrw0']").click()
    time.medium_timeout()


#get values from profile page
def get_number_posts_profile_page(driver):
    return fnum.string_to_number(driver.find_elements_by_xpath(".//span[@class = '_fd86t' ]")[0].text)

def get_number_followers_profile_page(driver):
    return fnum.string_to_number(driver.find_elements_by_xpath(".//span[@class = '_fd86t' ]")[1].text)

def get_number_following_profile_page(driver):
    return fnum.string_to_number(driver.find_elements_by_xpath(".//span[@class = '_fd86t' ]")[2].text)

def get_username_profile_page(driver):
    return driver.find_element_by_xpath(".//h1[@class = '_rf3jb notranslate']").text

def is_following_profile_page(driver):
    try:
        driver.find_element_by_xpath(".//button[@class = '_qv64e _t78yp _r9b8f _njrw0']");
        return True
    except Exception as e:
        return False



#follower / following panel
def get_all_users_popup_list(driver):
    ret_element = driver.find_elements_by_class_name("_6e4x5")
    time.medium_timeout()
    return ret_element

def click_username_popup_list(driver, element):
    element.find_element_by_xpath(".//a[@class = '_2g7d5 notranslate _o5iw8']").click()
    time.big_timeout()

def get_username_popup_list(driver, element):
    return element.find_element_by_xpath(".//a[@class = '_2g7d5 notranslate _o5iw8']").text

def is_following_popup_list(driver, element):
    try:
        # find following tag
        element.find_element_by_xpath(".//button[@class = '_qv64e _t78yp _4tgw8 _njrw0']");
        return True
    except Exception as e:
        return False
from General import time_utility as time


def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.medium_timeout()

def scroll_250(driver):
    driver.execute_script("scroll(0,250)")
    time.medium_timeout()
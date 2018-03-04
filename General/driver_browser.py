from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from General.settings import Setting as setting
from General import time_utility


def initialize_driver():
    _chrome_options = Options()
    _chrome_options.add_argument('disable-infobars')
    _chrome_options.add_argument(setting.user_data_path)

    driver = webdriver.Chrome(executable_path=setting.chrome_path, chrome_options=_chrome_options)
    driver.set_page_load_timeout(10)
    return driver

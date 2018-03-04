from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .settings import Setting as setting
from .time_utility import page_timeout

def initialize_driver():
    _chrome_options = Options()
    _chrome_options.add_argument('disable-infobars')
    _chrome_options.add_argument(setting.user_data_path)

    driver = webdriver.Chrome(executable_path=setting.chrome_path, chrome_options=_chrome_options)
    driver.set_page_load_timeout(page_timeout)
    return driver


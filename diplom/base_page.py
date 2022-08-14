from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select
from locators_page import *


class BasePage:
    def __init__(self, driver, url):
        self.chrome = driver
        self.url = url
        self.chrome.implicitly_wait(5)
        self.chrome.maximize_window()

    def open(self):
        self.chrome.get(self.url)

    def yellow_check(self):
        duck_name = self.chrome.find_element(*LocatorsPage.duck_name_loc).text
        if duck_name == "Yellow Duck":
            select = Select(self.chrome.find_element(*LocatorsPage.duck_size_loc))
            select.select_by_value('Small')
        time.sleep(1)

    def is_element_present(self, locator):
        try:
            if self.chrome.find_element(*locator):
                return True
        except NoSuchElementException:
            return False

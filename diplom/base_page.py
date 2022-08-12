from selenium import webdriver
from locators_page import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pytest


class BasePage:
    def __init__(self, driver, url):
        self.chrome = driver
        self.url = url
        self.chrome.implicitly_wait(5)
        self.chrome.maximize_window()

    def open(self):
        self.chrome.get(self.url)

    def is_element_present(self, locator):
        try:
            if self.chrome.find_element(*locator):
                return True
        except NoSuchElementException:
            return False




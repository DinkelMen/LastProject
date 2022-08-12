import time

from base_page import BasePage
from locators_page import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class EditAccountPage(BasePage):
    def edit_user_name(self):
        user_name = self.chrome.find_element(*MainPageLoc.user_name_loc)
        user_name.clear()
        time.sleep(2)
        user_name.send_keys("Full")

    def click_save_button(self):
        save_button = self.chrome.find_element(*MainPageLoc.save_button_loc)
        save_button.click()


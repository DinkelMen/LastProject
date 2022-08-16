from diplom.Pages.base_page import BasePage
from diplom.Pages.locators_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class DuckyPage(BasePage):
    def click_regional_settings(self):
        regional_settings = self.chrome.find_element(*LocatorsPage.regional_settings_loc)
        regional_settings.click()

    def login(self):
        email_address = self.chrome.find_element(*LocatorsPage.email_field_loc)
        password = self.chrome.find_element(*LocatorsPage.password_field_loc)
        login_button = self.chrome.find_element(*LocatorsPage.login_button)
        email_address.send_keys("bd@mail.ru")
        password.send_keys("12345")
        login_button.click()

    def add_ducks(self):
        purple_duck = self.chrome.find_element(*LocatorsPage.purple_duck_loc)
        purple_duck.click()
        time.sleep(3)

    def click_edit_account(self):
        edit_account = self.chrome.find_element(*LocatorsPage.edit_account_loc)
        edit_account.click()

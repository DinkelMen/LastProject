from base_page import BasePage
from locators_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import time


class DuckyPage(BasePage):
    def click_regional_settings(self):
        regional_settings = self.chrome.find_element(*MainPageLoc.regional_settings_loc)
        regional_settings.click()

    def login(self):
        email_address = self.chrome.find_element(*MainPageLoc.email_field_loc)
        password = self.chrome.find_element(*MainPageLoc.password_field_loc)
        login_button = self.chrome.find_element(*MainPageLoc.login_button)
        email_address.send_keys("bd@mail.ru")
        password.send_keys("12345")
        login_button.click()

    def add_ducks(self):
        purple_duck = self.chrome.find_element(*MainPageLoc.purple_duck_loc)
        purple_duck.click()
        time.sleep(3)

    def click_edit_account(self):
        edit_account = self.chrome.find_element(*MainPageLoc.edit_account_loc)
        edit_account.click()












# class DuckyPage(BasePage):
#     url = 'http://localhost/litecart/en/'
#
#     def open_ducky_page(self):
#         self.open()





# def test_case_1_group_1(open_browser):
#     chrome = browser
#     url = 'http://localhost/litecart/en/'
#     chrome.get(url)
#     chrome.fullscreen_window()
#     time.sleep(3)

# @allure.story('Allure story Test')
# def test():
#     chrome = webdriver.Chrome('./chromedriver')
#     try:
#         url = 'https://plugins.jenkins.io/shiningpanda'
#         chrome.get(url)
#         chrome.fullscreen_window()
#
#         element = WebDriverWait(chrome, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, '[class="title"]')))
#         text1 = element.text
#         assert text1 == "ShiningPanda"
#     finally:
#         time.sleep(3)
#         chrome.quit()
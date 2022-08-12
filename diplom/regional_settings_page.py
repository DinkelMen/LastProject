from base_page import BasePage
from locators_page import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class RegionalSettingsPage(BasePage):
    def set_country(self):
        country_list = self.chrome.find_element(*MainPageLoc.country_list_loc)
        country_list.click()
        # input_field = self.chrome.find_element(*MainPageLoc.country_input_field)
        # input_field.click()
        # input_field.sendkeys('Belarus')
        country_in_da_list = self.chrome.find_element(*MainPageLoc.country_in_da_list_loc)
        country_in_da_list.click()

    def set_currency(self):
        select = Select(self.chrome.find_element(*MainPageLoc.currency_loc))
        select.select_by_value('USD')

    def verify_country_currency(self):
        new_country = self.chrome.find_element(*MainPageLoc.country_list_loc)
        assert new_country.text == 'Belarus'
        new_currency = self.chrome.find_element(*MainPageLoc.currency_loc_2)
        assert new_currency.text == 'US Dollars'


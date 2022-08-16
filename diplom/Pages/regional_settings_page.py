from diplom.Pages.base_page import BasePage
from diplom.Pages.locators_page import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class RegionalSettingsPage(BasePage):
    def set_country(self):
        country_list = self.chrome.find_element(*LocatorsPage.country_list_loc)
        country_list.click()
        country_in_da_list = self.chrome.find_element(*LocatorsPage.country_in_da_list_loc)
        country_in_da_list.click()

    def set_currency(self):
        select = Select(self.chrome.find_element(*LocatorsPage.currency_loc))
        select.select_by_value('USD')

    def verify_country_currency(self):
        new_country = self.chrome.find_element(*LocatorsPage.country_list_loc)
        assert new_country.text == 'Belarus', f"new_country should be equal 'Belarus', got {new_country.text} instead"
        new_currency = self.chrome.find_element(*LocatorsPage.currency_loc_2)
        assert new_currency.text == 'US Dollars', f"new_currency should be equal 'US Dollars', got {new_currency.text} instead"

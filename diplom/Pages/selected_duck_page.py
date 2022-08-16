from diplom.Pages.base_page import BasePage
from diplom.Pages.locators_page import *
import time


class SelectedDuckPage(BasePage):

    def add_to_cart(self):
        self.yellow_check()
        add_to_cart_button = self.chrome.find_element(*LocatorsPage.add_to_cart_button_loc)
        add_to_cart_button.click()

    def add_to_cart_2(self):
        self.yellow_check()
        add_to_cart_button = self.chrome.find_element(*LocatorsPage.add_to_cart_button_loc_2)
        add_to_cart_button.click()

    def add_2_more(self):
        for n in [2, 3]:
            self.chrome.find_element(By.CSS_SELECTOR, f"#box-similar-products>:nth-child(2)>:nth-child(1)>:nth-child({n})>:nth-child(1)>:nth-child(1)>:nth-child(1)").click()
            self.yellow_check()
            self.add_to_cart()
            time.sleep(2)

    def go_to_cart(self):
        cart = self.chrome.find_element(*LocatorsPage.cart_loc)
        cart.click()

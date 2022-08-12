from base_page import BasePage
from locators_page import *
import time


class SelectedDuckPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.chrome.find_element(*MainPageLoc.add_to_cart_button_loc)
        add_to_cart_button.click()

    def add_2_more(self):
        for n in [2, 3]:
            self.chrome.find_element(By.CSS_SELECTOR, f"#box-similar-products>:nth-child(2)>:nth-child(1)>:nth-child({n})>:nth-child(1)>:nth-child(1)>:nth-child(1)").click()                                #box-similar-products>:nth-child(2)>:nth-child(1)>:nth-child(2)>:nth-child(1)>:nth-child(1)>:nth-child(1)
            self.add_to_cart()
            time.sleep(2)

    def go_to_cart(self):
        cart = self.chrome.find_element(*MainPageLoc.cart_loc)
        cart.click()

    # box - similar - products >: nth - child(2) >:nth - child(1) >: nth - child(2) >:nth - child(1) >: nth - child(1) >:nth - child(1)
    # def go_to_green(self):
    #     green_duck = self.chrome.find_element(*MainPageLoc.green_duck_lock)
    #     green_duck.click()
    #
    # def do_to_blue(self):
    #     blue_duck = self.chrome.find_element(*MainPageLoc.)
    #     blue_duck.click()



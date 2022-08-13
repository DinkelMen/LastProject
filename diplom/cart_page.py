import time

from base_page import BasePage
from locators_page import *


class CartPage(BasePage):
    def check_sum(self):
        summa = 0
        amount = 0
        for n in [2, 3, 4]:
            item = self.chrome.find_element(By.CSS_SELECTOR, f".dataTable>:nth-child(1)>:nth-child({n})>:nth-child(6)").text
            item = item[1:-2]
            summa += float(item)
            amount += 1
        act_sum = self.chrome.find_element(*MainPageLoc.actual_sum_loc).text
        act_sum = float(act_sum[1:-1])
        # print('dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd', summa, act_sum)
        assert summa == act_sum
        assert amount == 3

    def make_order(self):
        order_button = self.chrome.find_element(*MainPageLoc.order_button_loc)
        order_button.click()

    def change_amount(self):
        amount_window = self.chrome.find_element(*MainPageLoc.amount_window_loc)
        amount_window.clear()
        amount_window.send_keys('3')
        time.sleep(1)

    def click_update_button(self):
        update_button = self.chrome.find_element(*MainPageLoc.update_button_loc)
        update_button.click()
        time.sleep(1)

    def check_sum_2(self):
        act_sum = self.chrome.find_element(*MainPageLoc.actual_sum_2_loc).text
        act_sum = float(act_sum[1:-1])
        total_price = self.chrome.find_element(*MainPageLoc.total_price_loc).text
        total_price = float(total_price[1:-2])
        time.sleep(2)
        turtle_amount = self.chrome.find_element(*MainPageLoc.turtle_amount_loc).text
        time.sleep(1)
        # print('dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd', turtle_amount, act_sum, total_price)
        assert act_sum == total_price
        assert int(turtle_amount) == 3

    def remove_ducks(self):
        remove_button = self.chrome.find_element(*MainPageLoc.remove_button_lock)
        remove_button.click()
        time.sleep(2)

    def verify_cart_emptiness(self):
        page_message = self.chrome.find_element(*MainPageLoc.page_message_loc).text
        assert page_message == 'There are no items in your cart.'






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
        act_sum = self.chrome.find_element(*LocatorsPage.actual_sum_loc).text
        act_sum = float(act_sum[1:-1])
        assert summa == act_sum, f"summa should be equal 3, got {summa} instead"
        assert amount == 3, f"amount should be equal 3, got {amount} instead"

    def make_order(self):
        order_button = self.chrome.find_element(*LocatorsPage.order_button_loc)
        order_button.click()

    def change_amount(self):
        amount_window = self.chrome.find_element(*LocatorsPage.amount_window_loc)
        amount_window.clear()
        amount_window.send_keys('3')
        time.sleep(1)

    def click_update_button(self):
        update_button = self.chrome.find_element(*LocatorsPage.update_button_loc)
        update_button.click()
        time.sleep(1)

    def check_sum_2(self):
        act_sum = self.chrome.find_element(*LocatorsPage.actual_sum_2_loc).text
        act_sum = float(act_sum[1:-1])
        total_price = self.chrome.find_element(*LocatorsPage.total_price_loc).text
        total_price = float(total_price[1:-2])
        time.sleep(2)
        turtle_amount = self.chrome.find_element(*LocatorsPage.turtle_amount_loc).text
        time.sleep(1)

        assert act_sum == total_price, f"act_sum should be equal total_price, got act_sum = {act_sum} and total_price = {total_price}"
        assert int(turtle_amount) == 3, f"turtle_amount should be equal 3, got {turtle_amount} instead"

    def remove_ducks(self):
        remove_button = self.chrome.find_element(*LocatorsPage.remove_button_lock)
        remove_button.click()
        time.sleep(2)

    def verify_cart_emptiness(self):
        page_message = self.chrome.find_element(*LocatorsPage.page_message_loc).text
        assert page_message == 'There are no items in your cart.', f"page_message should be equal 'There are no items in your cart.', got {page_message} instead"

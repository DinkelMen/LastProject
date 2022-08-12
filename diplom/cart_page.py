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



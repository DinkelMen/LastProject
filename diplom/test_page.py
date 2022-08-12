import time
import pytest
from ducky_page import DuckyPage
from sql import SQL
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from regional_settings_page import RegionalSettingsPage
from selected_duck_page import SelectedDuckPage
from cart_page import CartPage
from api import API


@pytest.fixture
def open_chrome():
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.implicitly_wait(10)
    yield chrome
    chrome.quit()


def test_case_1(open_chrome):
    # Открываем главную страницу и переходим на Regional settings page по клику
    link = "http://localhost/litecart/en/"
    ducky_page = DuckyPage(open_chrome, link)
    ducky_page.open()
    time.sleep(3)
    ducky_page.click_regional_settings()
    # Меняем страну и валюту и проверяем это на UI
    # link2 = "http://localhost/litecart/en/regional_settings"
    rspage = RegionalSettingsPage(open_chrome, link)  # link2
    # rspage.open()
    rspage.set_country()
    rspage.set_currency()
    rspage.verify_country_currency()
    time.sleep(3)


def test_case_2(open_chrome):
    # Открываем приложение
    link = "http://localhost/litecart/en/"
    ducky_page = DuckyPage(open_chrome, link)
    ducky_page.open()
    time.sleep(1)
    # login
    ducky_page.login()
    time.sleep(3)
    # добавляем 3 утки в корзину и переходим в корзину
    ducky_page.add_ducks()
    selected_duck_page = SelectedDuckPage(open_chrome, link)
    selected_duck_page.add_to_cart()
    time.sleep(1)
    selected_duck_page.add_2_more()
    selected_duck_page.go_to_cart()
    time.sleep(3)
    # Проверяем что уточки добавились и цена верная
    cart_page = CartPage(open_chrome, link)
    cart_page.check_sum()
    cart_page.make_order()
    # Проверяем в БД что заказ сделан
    sql = SQL()
    sql.verify_order()


def test_api1():
    api = API()
    api.verify_api()





'''bd@mail.ru
+375223454343
12345'''


import time
import pytest
from diplom.Pages.ducky_page import DuckyPage
from diplom.sql import SQL
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from diplom.Pages.regional_settings_page import RegionalSettingsPage
from diplom.Pages.selected_duck_page import SelectedDuckPage
from diplom.Pages.cart_page import CartPage
from diplom.Pages.edit_account_page import EditAccountPage
import allure
from diplom.api import API


@pytest.fixture
def open_chrome():
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.implicitly_wait(10)
    yield chrome
    chrome.quit()


@allure.story('Changing the currency and country of the site')
def test_change_currency_country(open_chrome):
    with allure.step("Open the application and go to the Regional settings page by clicking"):
        link = "http://localhost/litecart/en/"
        ducky_page = DuckyPage(open_chrome, link)
        ducky_page.open()
        time.sleep(3)
        ducky_page.click_regional_settings()

    with allure.step("Change country and currency"):
        rspage = RegionalSettingsPage(open_chrome, link)
        rspage.set_country()
        rspage.set_currency()
    with allure.step("Check changes on the UI"):
        rspage.verify_country_currency()
        time.sleep(3)


@allure.story("Order creation and its verification in the database")
def test_order_creation_verification(open_chrome):
    with allure.step("Open the application"):
        link = "http://localhost/litecart/en/"
        ducky_page = DuckyPage(open_chrome, link)
        ducky_page.open()
        time.sleep(1)
    with allure.step("Log in to a pre-created user"):
        ducky_page.login()
        time.sleep(3)
    with allure.step("Add 3 duck to the cart and go there"):
        ducky_page.add_ducks()
        selected_duck_page = SelectedDuckPage(open_chrome, link)
        selected_duck_page.add_to_cart()
        time.sleep(1)
        selected_duck_page.add_2_more()
        selected_duck_page.go_to_cart()
        time.sleep(3)
    with allure.step("Verify that the ducks have been added and the price is correct"):
        cart_page = CartPage(open_chrome, link)
        cart_page.check_sum()
        cart_page.make_order()
    with allure.step("Check in the database that the order has been placed"):
        sql = SQL()
        sql.verify_order()


@allure.story("API Check of addition and removal pet")
def test_add_and_remove_pet():
    api = API()
    with allure.step("Add of new pet"):
        api.add_new_pet()
    with allure.step("Verify the addition of а pet"):
        api.check_new_pet()
    with allure.step("Delete the pet and check that it is absent"):
        api.delete_new_pet()


@allure.story("Change user name")
def test_change_user_name(open_chrome):
    with allure.step("Open the application"):
        link = "http://localhost/litecart/en/"
        ducky_page = DuckyPage(open_chrome, link)
        ducky_page.open()
        time.sleep(3)
    with allure.step("Log in"):
        ducky_page.login()
        time.sleep(3)
    with allure.step("Change user name"):
        ducky_page.click_edit_account()
        time.sleep(2)
        edit_account_page = EditAccountPage(open_chrome, link)
        edit_account_page.edit_user_name()
        edit_account_page.click_save_button()
    with allure.step("Check in the database that the name has been changed"):
        sql = SQL()
        sql.verify_name_change()


@allure.story("Order creation in another way, its verification and removal")
def test_order_another_create(open_chrome):
    with allure.step("Open the application"):
        link = "http://localhost/litecart/en/"
        ducky_page = DuckyPage(open_chrome, link)
        ducky_page.open()
        time.sleep(2)
    with allure.step("Add 1 duck"):
        ducky_page.add_ducks()
        selected_duck_page = SelectedDuckPage(open_chrome, link)
        selected_duck_page.add_to_cart_2()
        time.sleep(2)
    with allure.step("Go to cart"):
        selected_duck_page.go_to_cart()
        time.sleep(2)
        cart_page = CartPage(open_chrome, link)
    with allure.step("Change duck amount"):
        cart_page.change_amount()
        cart_page.click_update_button()
    with allure.step("Check that the ducks have been added and the price is correct"):
        cart_page.check_sum_2()
    with allure.step("Remove ducks"):
        cart_page.remove_ducks()
    with allure.step("Check if the cart is empty"):
        cart_page.verify_cart_emptiness()


@allure.story("API User creation and management")
def test_api2_user_create_manage():
    api = API()
    with allure.step("Create user"):
        api.create_user()
    with allure.step("Get user data"):
        api.get_user_data()
    with allure.step("Change user name"):
        api.change_user_name()
    with allure.step("Check if the name has changed"):
        api.check_user_name()

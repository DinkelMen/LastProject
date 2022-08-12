from selenium.webdriver.common.by import By


class MainPageLoc:
    regional_settings_loc = (By.CSS_SELECTOR, ".account>:nth-child(1)>:nth-child(2)>:nth-child(2)>:nth-child(1)")
    # regional_settings_bar_loc = (By.CSS_SELECTOR, "#box-regional-settings>:nth-child(1)")
    country_list_loc = (By.CSS_SELECTOR, ".select2-selection__rendered")
    currency_loc = (By.CSS_SELECTOR, "[name='currency_code']")
    currency_loc_2 = (By.CSS_SELECTOR, "[name='currency_code']>:nth-child(2)")
    # country_input_field = (By.CSS_SELECTOR, ".select2-search__field")
    country_in_da_list_loc = (By.CSS_SELECTOR, ".select2-results__options>:nth-child(21)")

    email_field_loc = (By.CSS_SELECTOR, "[name='email']")
    password_field_loc = (By.CSS_SELECTOR, "[name='password']")
    login_button = (By.CSS_SELECTOR, "[name='login']")

    purple_duck_loc = (By.CSS_SELECTOR, "#box-most-popular>:nth-child(2)>:nth-child(1)>:nth-child(1)>:nth-child(1)>:nth-child(1)>:nth-child(1)")
    add_to_cart_button_loc = (By.CSS_SELECTOR, "[type='submit']")

    green_duck_lock = (By.CSS_SELECTOR, "#box-similar-products>:nth-child(2)>:nth-child(1)>:nth-child(2)>:nth-child(1)>:nth-child(1)>:nth-child(1)")
    blue_duck_loc = (By.CSS_SELECTOR, "#box-similar-products>:nth-child(2)>:nth-child(1)>:nth-child(3)>:nth-child(1)>:nth-child(1)>:nth-child(1)")
    cart_loc = (By.CSS_SELECTOR, "#header>:nth-child(3)")  # переход со страницы последней утки в корзину

    actual_sum_loc = (By.CSS_SELECTOR, ".dataTable>:nth-child(1)>:nth-child(8)>:nth-child(2)>:nth-child(1)")

    order_button_loc = (By.CSS_SELECTOR, "[name='confirm_order']")






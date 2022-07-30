from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import allure
import time


@allure.story('Allure story Test')
def test():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = 'https://plugins.jenkins.io/shiningpanda'
        chrome.get(url)
        chrome.fullscreen_window()

        element = WebDriverWait(chrome, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, '[class="title"]')))
        text1 = element.text
        assert text1 == "ShiningPanda"
    finally:
        time.sleep(3)
        chrome.quit()

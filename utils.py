from time import sleep
from random import randint

from selenium.webdriver.common.by import By


PAUSE = randint(1, 4)


def input_key(browser, xpath, key=None):
    element = browser.find_element(By.XPATH, xpath)
    if key is not None:
        element.send_keys(key)
    sleep(PAUSE)


def click_button(browser, xpath):
    element = browser.find_element(By.XPATH, xpath)
    element.click()
    sleep(PAUSE)

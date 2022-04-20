from time import sleep
from random import randint


PAUSE = randint(1, 4)


def get_page(browser, url):
    browser.get(url)
    sleep(PAUSE)


def input_key(browser, xpath, key=None):
    browser.find_element('xpath', xpath).send_keys(key)
    sleep(PAUSE)


def click_button(browser, xpath):
    browser.find_element('xpath', xpath).click()
    sleep(PAUSE)

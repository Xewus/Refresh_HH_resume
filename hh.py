from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import constants as const
import utils


PHONE = ''
PASSWORD = ''


def main(browser):
    browser.get(const.HH_LOGIN_URL)
    browser.maximize_window()
    sleep(utils.PAUSE)

    utils.input_key(browser, const.PHONE_INPUT_XPATH, PHONE)
    utils.click_button(browser, const.PASSWWORD_XPATH)
    utils.input_key(browser, const.PASSWWORD_INPUT_XPATH, PASSWORD)
    utils.click_button(browser,  const.SUBMIT_BUTTON_XPATH)

    browser.get(const.RESUME_URL)
    sleep(utils.PAUSE)

    utils.click_button(browser, const.REFRESH_BUTTON_XPATH)
    sleep(9)

    browser.quit()


if __name__ == '__main__':
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    main(browser)

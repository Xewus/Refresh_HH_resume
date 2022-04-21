import datetime as dt
from time import sleep

from decouple import config
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import constants as const
import utils


PHONE = config('PHONE', default='')
PASSWORD = config('PASSWORD', default='')
RESUME_URL = config('RESUME_URL', default='')


def refresh_resume(browser):
    # Вход на строницу логина
    utils.get_page(browser, const.HH_LOGIN_URL)

    # Ввод номера телефона или почты
    utils.input_key(browser, const.PHONE_INPUT_XPATH, PHONE)

    # Переход на кнопку ввода пароля
    utils.click_button(browser, const.PASSWWORD_XPATH)

    # Ввод пароля
    utils.input_key(browser, const.PASSWWORD_INPUT_XPATH, PASSWORD)

    # Передача введённых данных
    utils.click_button(browser,  const.SUBMIT_BUTTON_XPATH)

    # Переход на страницу резюме
    browser.get(RESUME_URL)

    # Нажатие кнопки "Обновить"
    utils.click_button(browser, const.REFRESH_BUTTON_XPATH)

    browser.save_screenshot(
        '/Screenshots/resume_'
        f'{dt.datetime.now().strftime(const.DT_FORMAT)}.png'
    )

    browser.close()


if __name__ == '__main__':
    start_minutes, stop_minutes = utils.random_minutes()

    while True:
        utils.start_works()
        service = Service(executable_path=ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
        try:
            refresh_resume(browser)
        except ElementClickInterceptedException:
            sleep(60 * 30)
        finally:
            browser.quit()

        sleep(const.REFRESH_SECOND_PAUSE)
        sleep(start_minutes)
        start_minutes, stop_minutes = utils.random_minutes(
            start_minutes, stop_minutes
        )

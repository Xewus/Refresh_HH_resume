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
    """Обновляет резюме.

    Args:
        browser (_type_): _description_
    """
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
    errors_tries = const.ERROR_TRIES

    while errors_tries:
        utils.start_works()
        service = Service(executable_path=ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
        try:
            refresh_resume(browser)
            print('Refresh completed')
        except ElementClickInterceptedException:
            errors_tries -= 1
            browser.quit()
            print('errs=', errors_tries)
            sleep(60 * 30)
        finally:
            browser.quit()

        utils.wait(start_minutes)
        start_minutes, stop_minutes = utils.random_minutes(
            start_minutes, stop_minutes
        )
    print('Допущено 3 ошибки')

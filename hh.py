from time import sleep, time
from random import randint

from selenium import webdriver
# Импортируем классы для Chrome. Если у вас другой браузер - измените импорт.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import constants as const


USERNAME = ''
PASSWORD = ''
PAUSE = randint(1, 4)

service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
browser.get(const.HH_LOGIN_URL)
browser.maximize_window()
sleep(PAUSE)

phone_input = browser.find_element(By.XPATH, const.PHONE_INPUT_XPATH)
phone_input.send_keys(USERNAME)
sleep(PAUSE)

goto_password = browser.find_element(By.XPATH, const.PASSWWORD_XPATH)
goto_password.click()
sleep(PAUSE)

password_input = browser.find_element(By.XPATH, const.PASSWWORD_INPUT_XPATH)
password_input.send_keys(PASSWORD)
sleep(PAUSE)

submit_button = browser.find_element(By.XPATH, const.SUBMIT_BUTTON_XPATH)
submit_button.click()
sleep(PAUSE)

browser.get(const.RESUME_URL)
sleep(PAUSE)

refresh = browser.find_element(By.XPATH, const.REFRESH_BUTTON_XPATH)
refresh.click()
sleep(9)

browser.quit()

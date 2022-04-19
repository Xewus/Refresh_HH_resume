from time import sleep, time
from random import randint

from selenium import webdriver
# Импортируем классы для Chrome. Если у вас другой браузер - измените импорт.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


HH_LOGIN_URL = 'https://spb.hh.ru/account/login?backurl=%2F'
RESUME_URL = 'https://spb.hh.ru/resume/e7b22514ff0971ecc00039ed1f6e3968595254'
USERNAME = ''
PASSWORD = ''
PAUSE = randint(1, 4)

service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
browser.get(HH_LOGIN_URL)
browser.maximize_window()
sleep(PAUSE)

login_input = browser.find_element(By.XPATH, '//input[@placeholder="Email или телефон"]')
login_input.send_keys(USERNAME)
sleep(3)

goto_password = browser.find_element(By.XPATH, '//button[@data-qa="expand-login-by-password"]')
goto_password.click()
sleep(PAUSE)

password_input = browser.find_element(By.XPATH, '//input[@placeholder="Пароль"]')
password_input.send_keys(PASSWORD)
sleep(PAUSE)

submit_button = browser.find_element(By.XPATH, '//button[@data-qa="account-login-submit"]')
submit_button.click()
sleep(PAUSE)

browser.get(RESUME_URL)
sleep(PAUSE)

refresh = browser.find_element(By.XPATH, '//button[@data-qa="resume-update-message"]')
refresh.click()
sleep(9)

browser.quit()

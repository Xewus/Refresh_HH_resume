DT_FORMAT = '%d/%m/%y_%H:%M'

HH_LOGIN_URL = 'https://spb.hh.ru/account/login?backurl=%2F'

PHONE_INPUT_XPATH = '//input[@placeholder="Email или телефон"]'
PASSWWORD_XPATH = '//button[@data-qa="expand-login-by-password"]'
PASSWWORD_INPUT_XPATH = '//input[@placeholder="Пароль"]'
SUBMIT_BUTTON_XPATH = '//button[@data-qa="account-login-submit"]'
REFRESH_BUTTON_XPATH = '//button[contains(., "Обновить дату")]'
TIME_OUT_XPATH = '//*[contains(., "Обновить можно через")]'
RE_TIME_OUT_HOUR = r'(Обновить можно через) (.*час.\.)'
RE_TIME_OUT_MINUTE = r'(Обновить можно через) (\b\d{0,2} минут)'

REFRESH_HOUR_PAUSE = 4
REFRESH_SECOND_PAUSE = 60 * 60 * REFRESH_HOUR_PAUSE
START_WORKS = 8  # 8 hours AM

import datetime as dt
import re
from random import randint
from time import sleep

import constants as const

PAUSE = randint(1, 4)


def random_minutes(start=0, stop=10):
    """Устанавливает случайные значения, для возможной
     проверки на повторяемость периодов обновления.

    Args:
        start (int, optional): Начальное значение.
                               Defaults to 0.
        stop (int, optional): Граничное значение.
                              Defaults to 10.

    Returns:
        tuple(int, int): Кортеж из случайных чисел от 0 до 59.
    """
    start = randint(start, stop)
    if start > 59:
        start = 0
    stop = randint(start, 10)
    return start, stop


def start_works():
    """Вычисляет время для старта скрипта.

    В случае, если текущее время (в часах) больше 0,
    но меньше установленного для начала работы - ожидает
    наступления установленного часа.
    """
    difference = const.START_WORKS - dt.datetime.now().hour
    if difference <= 0:
        return
    sleep(difference * 60 * 60)


def wait(minutes=0):
    """Останавливает выполнение скрипта.

    Программа остановливается на установленное количество
    часов и случайное количество минут.

    Args:
        minutes (int, optional): Количество минут для задержки.
                                 Defaults to 0.
    """
    sleep(const.REFRESH_SECOND_PAUSE)
    sleep(minutes * 60)


def get_page(browser, url):
    """Переходит на страницу с указанным url.

    Args:
        browser (_type_): _description_
        url (str): url страницы.
    """
    browser.get(url)
    sleep(PAUSE)


def find_element(browser, xpath):
    """Находит элемент html-документа по xpath.

    Args:
        browser (_type_): _description_
        xpath (str): _description_

    Returns:
        _type_: Найденный элемент.
        None: Если элемент не найден.
    """
    element = browser.find_element('xpath', xpath)
    return element


def input_key(browser, xpath, key):
    """Вводит переданное значение.

    Args:
        browser (_type_): _description_
        xpath (str): xpath для поиска элемента.
        key (str): Значение для ввода.
    """
    find_element(browser, xpath).send_keys(key)
    sleep(PAUSE)


def click_button(browser, xpath):
    """Нажимает кнопку.

    Args:
        browser (_type_): _description_
        xpath (str): xpath для поиска кнопки.
    """
    find_element(browser, xpath).click()
    sleep(PAUSE)


def find_time_out(browser, xpath):
    """Находит оставшееся время до следующего обновления.

    Args:
        browser (_type_): _description_
        xpath (str): xpath для поиска оставшегося времени.

    Returns:
        int: Оставшееся количество часов до обновления.
    """
    text = find_element(browser, xpath)
    time_out = re.search(const.RE_TIME_OUT_HOUR, text)

    time_out = time_out.group(2)

    if time_out is not None:
        time_out = time_out.group(2)
        if time_out[0].isdecimal():
            return time_out.split()[0]
    return 0

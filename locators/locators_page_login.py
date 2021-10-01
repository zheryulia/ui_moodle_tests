"""
Уникальные идентификаторы страницы авторизации.
"""

from selenium.webdriver.common.by import By


class LocatorsPageLogin:

    CONFIRM_EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    EXIT = (By.ID, "actionmenuaction-6")
    LOGIN = (By.ID, "username")
    LOGIN_BUTTON = (By.ID, "loginbtn")
    PASSWORD = (By.ID, "password")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    USER_MENU = (By.CLASS_NAME, "usermenu")
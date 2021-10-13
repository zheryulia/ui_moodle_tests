"""
Уникальные идентификаторы страницы авторизации.
"""

from selenium.webdriver.common.by import By


class LocatorsPageLogin:

    CONFIRM_EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    EXIT = (By.ID, "actionmenuaction-6")
    LOGIN = (By.ID, "username")
    LOGIN_BUTTON = (By.ID, "loginbtn")
    LOGIN_ERRORMESSAGE = (By.ID, "loginerrormessage")
    PASSWORD = (By.ID, "password")
    PERSONAL_ACCOUNT = (By.ID, "actionmenuaction-1")
    RECENT_COURSES = (By.ID, "instance-189-header")
    USERNAME = (By.ID, "username")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    USER_MENU_SETTINGS = (By.ID, "actionmenuaction-5")

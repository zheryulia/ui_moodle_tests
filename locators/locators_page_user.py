"""
Уникальные идентификаторы страницы пользователя.
"""

from selenium.webdriver.common.by import By


class LocatorsUserMain:
    EDIT_INFO = (By.LINK_TEXT, "Редактировать информацию")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    USER_MENU_SETTINGS = (By.ID, "actionmenuaction-5")


class LocatorsPageUser:
    CITY_INPUT = (By.ID, "id_city")
    DATA_CHANGED_ALERT = (
        By.XPATH,
        "//div[@class='alert alert-success alert-block fade in ']",
    )
    EMAIL = (By.ID, "id_email")
    SUBMIT_BUTTON = (By.ID, "id_submitbutton")

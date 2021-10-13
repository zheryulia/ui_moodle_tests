"""
Уникальные идентификаторы страницы курсов.
"""

from selenium.webdriver.common.by import By


class LocatorsPageCourseManagement:
    CREATE_NEW_COURSE = (By.LINK_TEXT, "Создать новый курс")
    SEARCH = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//*[contains(@class,'icon fa fa-search fa-fw')]")
    SEARCH_RESULT = (
        By.XPATH,
        "//*[contains(@class,'listing-pagination-totals text-muted')]",
    )
    DELETE = (By.XPATH, "//*[contains(@class,'icon fa fa-trash fa-fw')]")


class LocatorsPageCourseEdit:
    FULL_NAME = (By.ID, "id_fullname")
    SHORT_NAME = (By.ID, "id_shortname")
    SAVE_AND_DISPLAY = (By.ID, "id_saveanddisplay")
    ERROR_SHORT_NAME = (By.ID, "id_error_shortname")


class LocatorsPageCourseDelete:
    BUTTON_DELETE = (By.XPATH, "//*[contains(@class,'btn btn-primary')]")

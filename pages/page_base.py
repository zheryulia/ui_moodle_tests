"""
Здесь содержится весь повторяющийся код,
который перемещается в класс и действует как родительский класс для всех других классов.
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Не удается найти элемент по локатору {locator}",
        )
        return element

    def find_elements(self, locator):
        return self.app.driver.find_elements(*locator)

    def select_value(self, select_element, value):
        select_element.select_by_value(value)

    def find_element_by_link_text(self, locator):
        return WebDriverWait(self.app.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )

    def click_on_link(self, locator):
        return (
            WebDriverWait(self.app.driver, 20)
            .until(EC.element_to_be_clickable(locator))
            .click()
        )

    def click_on_button(self, locator):
        return (
            WebDriverWait(self.app.driver, 20)
            .until(EC.visibility_of_element_located(locator))
            .click()
        )

    @staticmethod
    def set_value_select(element, value):
        return Select(element).select_by_visible_text(value)

    @staticmethod
    def fill_element(element, text):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    @staticmethod
    def click_element(element):
        element.click()

    @staticmethod
    def clear_element(element):
        element.clear()

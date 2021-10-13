"""
Работа со страницей авторизации.
"""

from models.auth import AuthData
from pages.page_base import BasePage
from locators.locators_page_login import LocatorsPageLogin


class LoginPage(BasePage):
    """Page to check login of users."""

    def is_auth(self):
        """Проверка, что вход был осуществлен."""

        element = self.find_elements(LocatorsPageLogin.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def confirm_exit_window(self):
        element = self.find_elements(LocatorsPageLogin.CONFIRM_EXIT_BUTTON)
        if len(element) > 0:
            return True
        return False

    def check_personal_account(self):
        return self.find_element(LocatorsPageLogin.PERSONAL_ACCOUNT)

    def find_error_message(self):
        return self.find_element(LocatorsPageLogin.LOGIN_ERRORMESSAGE)

    def user_menu(self):
        return self.find_element(LocatorsPageLogin.USER_MENU)

    def user_menu_settings(self):
        return self.find_element(LocatorsPageLogin.USER_MENU_SETTINGS)

    def auth(self, data):
        """Функция входа в личный кабинет."""

        login = data.login
        password = data.password
        self.fill_element(self.find_element(LocatorsPageLogin.USERNAME), login)
        self.fill_element(self.find_element(LocatorsPageLogin.PASSWORD), password)
        self.click_element(self.find_element(LocatorsPageLogin.LOGIN_BUTTON))

    def sign_out(self):
        """Выйти из системы."""

        if self.is_auth():
            self.click_element(self.find_element(LocatorsPageLogin.USER_MENU))
            self.click_element(self.find_element(LocatorsPageLogin.EXIT))
        if self.confirm_exit_window():
            self.click_element(self.find_element(LocatorsPageLogin.CONFIRM_EXIT_BUTTON))

"""
Работа со страницей пользователя.
"""

# from models.user_data import AuthData
from pages.page_base import BasePage
from locators.locators_page_user import LocatorsPageUser, LocatorsUserMain


class UserPage(BasePage):
    def user_menu(self):
        return self.find_element(LocatorsUserMain.USER_MENU)

    def user_menu_settings(self):
        return self.find_element(LocatorsUserMain.USER_MENU_SETTINGS)

    def edit_user_data(self):
        self.click_element(self.user_menu())
        self.click_element(self.user_menu_settings())
        self.click_element(self.find_element(LocatorsUserMain.EDIT_INFO))


class UserDataPage(BasePage):
    def submit_button(self):
        return self.find_element(LocatorsPageUser.SUBMIT_BUTTON)

    def input_city(self):
        return self.find_element(LocatorsPageUser.CITY_INPUT)

    def add_input_city(self, city):
        self.fill_element(self.input_city(), city)

    def save_user_data(self):
        self.click_element(self.submit_button())

    def add_edit_user_data(self, data):
        self.add_input_city(data.city)
        self.save_user_data()

    def find_email_field(self):
        return self.find_element(LocatorsPageUser.EMAIL)

    def clear_email(self):
        self.clear_element(self.find_email_field())

    def has_data_changed_alert(self):
        """Сообщение что данные изменены"""
        return len(self.find_elements(LocatorsPageUser.DATA_CHANGED_ALERT)) != 0

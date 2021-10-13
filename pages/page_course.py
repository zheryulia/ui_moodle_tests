"""
Работа со страницей курсов.
"""

from pages.page_base import BasePage

from selenium.webdriver.common.by import By

from locators.locators_page_course import LocatorsPageCourseManagement
from locators.locators_page_course import LocatorsPageCourseEdit
from locators.locators_page_course import LocatorsPageCourseDelete


class CourseManagementPage(BasePage):
    def find_course_name(self, name):
        locator = (By.LINK_TEXT, name)
        return self.find_element_by_link_text(locator)

    def delete(self):
        return self.find_element(LocatorsPageCourseManagement.DELETE)

    def click_delete_icon(self):
        self.click_element(self.delete())

    def find_search_field(self):
        return self.find_element(LocatorsPageCourseManagement.SEARCH)

    def click_on_search_button(self):
        self.click_on_button(LocatorsPageCourseManagement.SEARCH_BUTTON)

    def search_result(self):
        return self.find_element(LocatorsPageCourseManagement.SEARCH_RESULT)


class CourseEditPage(BasePage):
    def find_full_name_field(self):
        return self.find_element(LocatorsPageCourseEdit.FULL_NAME)

    def find_short_name_field(self):
        return self.find_element(LocatorsPageCourseEdit.SHORT_NAME)

    def save_and_show_button(self):
        return self.find_element(LocatorsPageCourseEdit.SAVE_AND_DISPLAY)

    def find_error_message_about_short_name(self):
        return self.find_element(LocatorsPageCourseEdit.ERROR_SHORT_NAME)

    def submit_changes(self):
        self.click_element(self.save_and_show_button())


class CourseDeletePage(BasePage):
    def confirm_delete(self):
        self.click_on_button(LocatorsPageCourseDelete.BUTTON_DELETE)

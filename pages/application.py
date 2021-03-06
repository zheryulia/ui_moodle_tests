"""
Здесь содержатся основные действия над сайтом.
"""

from pages.page_login import LoginPage
from pages.page_user import UserPage, UserDataPage
from pages.page_course import CourseManagementPage, CourseEditPage, CourseDeletePage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.user_data = UserPage(self)
        self.user_data_page = UserDataPage(self)
        self.course_mng = CourseManagementPage(self)
        self.course_edit = CourseEditPage(self)
        self.course_del = CourseDeletePage(self)

    def quit(self):
        self.driver.quit()

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")

    def open_create_course_page(self):
        self.driver.get(self.url + "/course/edit.php")

    def open_mng_course_page(self):
        self.driver.get(self.url + "/course/management.php")

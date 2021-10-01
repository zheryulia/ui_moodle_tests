"""
Здесь содержатся основные ействия над сайтом.
"""


from pages.page_login import LoginPage
from pages.page_user import UserPage, UserDataPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.user_data = UserPage(self)
        self.user_data_page = UserDataPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")



"""
Тесты на изменение данных в аккаунте пользователя.
"""
import pytest

from models.user_data import UserData
from models.auth import AuthData
from time import sleep


class TestAddPersonalData:

    def test_update_user_data(self, app):
        """
        Шаги:
        1. Авторизоваться на портале.
        2. Перейти в меню редактирования профиля.
        3. Сгенерировать название города.
        4. Заполнить поля с данными.
        5. Сохранить изменения.

        Оиждаемый результат:
        1. Вышло сообщение об успешном изменении.
        """

        app.open_auth_page()
        data = AuthData(login="yuliazher", password="Yul343!!")
        app.login.auth(data)
        app.user_data.edit_user_data()
        change_user_data = UserData.random()
        app.user_data_page.add_edit_user_data(change_user_data)

    def test_empty_user_data(self, app):
        """
        Шаги:
        1. Авторизоваться на портале.
        2. Перейти в меню редактирования профиля.
        3. Отчистить поле email.
        4. Сохранить изменения.

        Оиждаемый результат:
        1. Вышло редупреждение.
        """

        app.open_auth_page()
        data = AuthData(login="yuliazher", password="Yul343!!")
        app.login.auth(data)
        app.user_data.edit_user_data()
        app.user_data_page.clear_email()
        app.user_data_page.save_user_data()
        sleep(5)
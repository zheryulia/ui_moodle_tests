"""
Тесты на изменение данных в аккаунте пользователя.
"""

import allure

from models.user_data import UserData
from models.auth import AuthData


class TestAddPersonalData:
    @allure.story("Позитивный тест")
    def test_update_user_data(self, app):
        """
        Шаги:
        1. Авторизоваться на портале.
        2. Перейти в меню редактирования профиля.
        3. Сгенерировать название города.
        4. Заполнить поле с данными.
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
        with allure.step("Проверяем авторизацию с валидными данными"):
            assert (app.login.check_personal_account()
            ), "Данные не изменены"
        app.login.sign_out()

    @allure.story("Негативный тест")
    def test_empty_user_data(self, app):
        """
        Шаги:
        1. Авторизоваться на портале.
        2. Перейти в меню редактирования профиля.
        3. Отчистить поле email.
        4. Сохранить изменения.

        Оиждаемый результат:
        1. Вышло предупреждение.
        """

        app.open_auth_page()
        data = AuthData(login="yuliazher", password="Yul343!!")
        app.login.auth(data)
        app.user_data.edit_user_data()
        app.user_data_page.clear_email()
        app.user_data_page.save_user_data()
        with allure.step("Проверяем авторизацию с пустым логином"):
            assert (not app.user_data_page.has_data_changed_alert()
            ), "Данные были изменены!"
        app.login.sign_out()

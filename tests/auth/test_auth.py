"""
Тесты на вход в аккаунт пользователем.
"""

import allure
import pytest

from models.auth import AuthData


class TestAuth:
    @allure.story("Позитивный тест")
    def test_auth_valid_data(self, app):
        """
        Шаги:
        1. Открыть главную страницу.
        2. Вести корректные данные (пример: login="yuliazher", password="Yul343!!").

        Ожидаемый реузльтат:
        1. Успешный вход.
        """
        app.open_auth_page()
        data = AuthData(login="yuliazher", password="Yul343!!")
        app.login.auth(data)
        with allure.step("Проверяем авторизацию с валидными данными"):
            assert (app.login.check_personal_account()
            ), "Вход невозможен"
        app.login.sign_out()

    @allure.story("Негативный тест")
    def test_auth_invalid_data(self, app):
        """
        Шаги:
        1. Открыть главную страницу
        2. Вести НЕ корректные данные (используем генерацию случайных данных)

        Ожидаемый реузльтат:
        1. Появилось сообщение об ошибке
        """
        app.open_auth_page()
        data = AuthData.random()
        app.login.auth(data)
        with allure.step("Проверяем авторизацию с невалидным логином"):
            assert (app.login.find_error_message()
            ), "Удалось войти!"
        app.login.sign_out()

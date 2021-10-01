"""
Тесты на вход в аккаунт пользователем.
"""
import pytest

from models.auth import AuthData


class TestAuth:
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

    @pytest.mark.parametrize("field", ["login", "password"])  # параметризирует аргументы тестовых функций
    def test_auth_empty_data(self, app, field):
        """
        Шаги:
        1. Открыть главную страницу
        2. Оставить поле ввода пустым

        Ожидаемый реузльтат:
        1. Появилось сообщение об ошибке
        """
        app.open_auth_page()
        data = AuthData.random()
        setattr(data, field, None)  # добавляет объекту указанный аттрибут None

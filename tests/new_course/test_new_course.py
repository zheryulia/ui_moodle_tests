"""
Тесты на создание новых курсов.
"""

import allure
import pytest

from models.course import NewCourse
from models.auth import AuthData


class TestAddNewCourse:

    @allure.story("Позитивный тест")
    def test_valid_course_creation(self, app):
        """
        Предусловие:
        1. У пользователя, под которым вы авторизуетесь, есть права администратора

        Шаги:
        1. Авторизоваться на портале.
        2. Перейти в меню создания курса.
        3. Добавить курс.
        4. Заполнить полное название курса.
        5. Заполнить краткое название курса.
        6. Сохранить.

        Ожидаемый результат:
        1. Курс успешно создан.
        """
        app.open_auth_page()
        data = AuthData(login="yuliazher", password="Yul343!!")
        app.login.auth(data)
        app.open_create_course_page()
        full_name_field = app.course_edit.find_full_name_field()
        full_name = NewCourse.random().full_name
        app.course_edit.fill_element(full_name_field, full_name)
        short_name_field = app.course_edit.find_short_name_field()
        short_name = NewCourse.random().short_name
        app.course_edit.fill_element(short_name_field, short_name)
        app.course_edit.submit_changes()
        with allure.step("Проверяем позитивный кейс создания нового курса"):
            app.open_mng_course_page()
            search_field = app.course_mng.find_search_field()
            app.course_mng.fill_element(search_field, full_name)
            app.course_mng.click_on_search_button()
            assert app.course_mng.search_result()
        app.course_mng.find_course_name(full_name)
        app.course_mng.click_delete_icon()
        app.course_del.confirm_delete()
        app.login.sign_out()

    @allure.story("Негативный тест")
    def test_invalid_course_creation(self, app):
        """
        Предусловие:
        1. У пользователя, под которым вы авторизуетесь, есть права администратора

        Шаги:
        1. Авторизоваться на портале.
        2. Перейти в меню создания курса.
        3. Добавить курс.
        4. Заполнить полное название курса.
        5. Оставить пустым краткое название курса.
        6. Сохранить.

        Ожидаемый результат:
        1. Отображается предупреждение.
        """
        app.open_auth_page()
        data = AuthData(login="yuliazher", password="Yul343!!")
        app.login.auth(data)
        app.open_create_course_page()
        full_name_field = app.course_edit.find_full_name_field()
        full_name = NewCourse.random().full_name
        app.course_edit.fill_element(full_name_field, full_name)
        app.course_edit.submit_changes()
        with allure.step("Проверяем негативный кейс создания нового курса"):
            assert app.course_edit.find_error_message_about_short_name()
        app.login.sign_out()

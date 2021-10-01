import pytest

from models.course import CreateCourse
from models.auth import AuthData


class TestAddNewCourse:
    """Adding new courses."""

    @pytest.mark.xfail
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
        data = AuthData.random()
        app.login.auth(data)
        app.open_create_course_page()
        course_info = CreateCourse.random()
        app.create_course.create_course(course_info)

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        "full_course_name, short_course_name",
        [
            [CreateCourse.random().full_course_name, None],
            [None, CreateCourse.random().short_course_name],
        ],
    )
    def test_invalid_course_creation(
        self, app, full_course_name, short_course_name
    ):
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
        data = AuthData.random()
        app.login.auth(data)
        app.open_create_course_page()
        course_info = CreateCourse.random()
        setattr(course_info, "full_course_name", full_course_name)
        setattr(course_info, "short_course_name", short_course_name)
        app.create_course.create_course(course_info)
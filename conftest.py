import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    """Фикстура для открытия браузера."""

    url = request.config.getoption("--url")
    headless_type = request.config.getoption("--headless").lower()
    if headless_type == "true":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
            url,
        )
    else:
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install()), url
        )
    yield fixture
    # Чистим после себя
    fixture.quit()


@pytest.fixture
def auth(app, request):
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")
    app.open_auth_page()
    auth_data = AuthData(login=login, password=password)
    app.login.auth(auth_data)
    assert app.login.is_auth(), "Вход не выполнен"
    yield
    app.login.sign_out()


def pytest_addoption(parser):
       parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="'true' для режима без видимого браузера,\n"
        "'false' - для режима где браузер виден",
        ),
        parser.addoption(
            "--url",
            action="store",
            default="https://qacoursemoodle.innopolis.university",
            help="ссылка на qacourse",
        )
            parser.addoption(
            "--login",
            action="store",
            default="yuliazher",
            help="имя пользователя",
        ),
        parser.addoption(
            "--password",
            action="store",
            default="Yul343!!",
            help="пароль",
        )

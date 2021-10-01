import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--url")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    fixture = Application(
        webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
        url,
    )
    yield fixture
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
        "--url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="ссылка на qacourse",
    )

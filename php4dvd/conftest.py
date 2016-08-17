# -*- coding: utf-8 -*-

import allure
import pytest

from conf import config
from tools import browsers
from pages.home import HomePage
from pages.auth import AuthPage


# опции командной строки

def pytest_addoption(parser):
    """Дополнительные опции командной строки вызова py.test"""
    parser.addoption('--browser', action='store', default=config.DEFAULT_BROWSER,
                     help='Browser type')
    parser.addoption('--remote', action='store_true', help='Use the remote browser')
    parser.addoption('--no-remote', action='store_false', help='Do not use the remote browser')
    parser.addoption('--selenium-hub', action='store', default='',
                     help='Hub URL of Selenium-Grid')
    parser.addoption('--base-url', action='store', default=config.BASE_URL,
                     help='Base URL for SUT/AUT')


@pytest.fixture(scope='session')
def browser_type(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--base-url')


@pytest.fixture(scope='session')
def remote(request):
    if request.config.getoption('--remote') is True:
        return True
    if request.config.getoption('--no-remote') is False:
        return False
    return False


@pytest.fixture(scope='session')
def selenium_hub(request, remote):
    hub = request.config.getoption('--selenium-hub')
    if remote and not hub:
        raise Exception('--selenium-hub option is required with --remote option')
    return hub


#

@pytest.yield_fixture(scope='session')
def driver(browser_type, base_url, remote, selenium_hub):
    """Драйвер браузера"""
    if browser_type == 'firefox':
        browser = browsers.get_firefox(remote=remote, selenium_hub=selenium_hub)
    else:
        raise ValueError('Browser "{:s}" not supported'.format(browser_type))
    allure.environment(
        browser=browser.capabilities['browserName'],
        version=browser.capabilities['version'],
        platform=browser.capabilities['platform'],
    )
    browsers.set_webdriver(browser)
    browser.maximize_window()
    browser.get(base_url)
    yield browser
    browser.quit()


@pytest.fixture(scope='class')
def wd(request, driver):
    request.cls.driver = driver


@pytest.fixture(scope='session')
def admin():
    class User(object):
        login = config.USER
        password = config.PASSWORD
    return User


@pytest.yield_fixture(scope='class')
def login(driver, admin):
    """Вход в систему"""
    page = AuthPage(driver)
    page.username = admin.login
    page.password = admin.password
    page.click_login_button()
    yield


@pytest.yield_fixture(scope='class')
def logout(driver):
    """Выход из системы"""
    yield
    HomePage(driver).nav.click_logout_button()

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
    parser.addoption('--base-url', action='store', default=config.BASE_URL,
                     help='Browser type')


@pytest.fixture(scope='session')
def browser_type(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--base-url')


#

@pytest.yield_fixture(scope='session')
def driver(browser_type):
    """Драйвер браузера"""
    if browser_type == 'firefox':
        browser = browsers.get_firefox()
    else:
        raise ValueError('Browser "{:s}" not supported'.format(browser_type))
    allure.environment(
        browser=browser.capabilities['browserName'],
        version=browser.capabilities['version'],
        platform=browser.capabilities['platform'],
    )
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
    driver.get(config.BASE_URL)
    page = AuthPage(driver)
    page.username = admin.login
    page.password = admin.password
    page.click_login_button()
    yield


@pytest.yield_fixture(scope='class')
def logout(driver):
    """Выход из системы"""
    yield
    driver.get(config.BASE_URL)
    HomePage(driver).nav.click_logout_button()

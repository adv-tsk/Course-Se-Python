# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By

from conf import config
from tools import browsers
from tools.wraps import find_element


@pytest.yield_fixture(scope='session')
def driver():
    """Драйвер браузера"""
    wd = browsers.get_firefox()
    allure.environment(browser='Mozilla Firefox')
    yield wd
    wd.quit()


@pytest.fixture(scope='class')
def wd(request, driver):
    request.cls.driver = driver


@pytest.yield_fixture(scope='class')
def login(driver):
    """Вход в систему"""
    driver.get(config.BASE_URL)
    with allure.step('Вход в систему'):
        find_element(driver, (By.ID, 'username')).send_keys(config.USER)
        find_element(driver, (By.NAME, 'password')).send_keys(config.PASSWORD)
        find_element(driver, (By.NAME, 'submit')).click()
    yield


@pytest.yield_fixture(scope='class')
def logout(driver):
    """Выход из системы"""
    yield
    driver.get(config.BASE_URL)
    with allure.step('Выход из системы'):
        find_element(driver, (By.LINK_TEXT, 'Log out')).click()
    driver.switch_to.alert.accept()

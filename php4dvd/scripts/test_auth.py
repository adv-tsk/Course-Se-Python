# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

from conf import config
from tools.wraps import find_element


@allure.feature('Вход пользователя в систему')
@pytest.mark.usefixtures('wd', 'logout')
class TestSignIn(object):
    """Набор тестов входа пользователя в систему"""

    @allure.story('Аутентификация')
    @pytest.mark.parametrize(
        'login, password, result',
        [('anonymous', 'hackyoursite', True),
         (config.USER, config.PASSWORD, False)]
    )
    def test_signin(self, login, password, result):
        self.driver.get(config.BASE_URL)

        with allure.step('Ввод логина'):
            username = find_element(self.driver, (By.ID, 'username'))
            username.send_keys(login)
        with allure.step('Ввод пароля'):
            _password = find_element(self.driver, (By.NAME, 'password'))
            _password.send_keys(password)
        with allure.step('Нажимаем "Войти"'):
            find_element(self.driver, (By.NAME, 'submit')).click()

        assert self.has_error_message() is result

    def has_error_message(self):
        try:
            find_element(self.driver, (By.CSS_SELECTOR, 'td[class="error"]'))
        except TimeoutException:
            return False
        else:
            return True


@allure.feature('Выход пользователя из системы')
@pytest.mark.usefixtures('wd', 'login')
class TestLogOut(object):
    """Набор тестов выхода пользователя из системы"""

    @allure.story('Выход из системы')
    def test_logout(self):
        self.driver.get(config.BASE_URL)

        with allure.step('Нажимаем на ссылку "Log out"'):
            find_element(self.driver, (By.LINK_TEXT, 'Log out')).click()

        assert self.is_alert_present() is True
        assert self.close_alert_and_get_its_text() == 'Are you sure you want to log out?'

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

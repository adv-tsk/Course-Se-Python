# -*- coding: utf-8 -*-

import allure
import pytest

from conf import config
from pages.auth import AuthPage
from pages.home import HomePage


@allure.feature('Вход пользователя в систему')
@pytest.mark.usefixtures('wd', 'logout')
class TestSignIn(object):
    """Набор тестов входа пользователя в систему"""

    @allure.story('Аутентификация не существующего пользователя')
    def test_signin_not_existing_user(self, user_not_exists):
        user = user_not_exists

        self.driver.get(config.BASE_URL)

        page = AuthPage(self.driver)
        page.username = user.login
        page.password = user.password
        page.click_login_button()

        assert page.user_is_not_signin()

    @allure.story('Аутентификация существующего пользователя')
    def test_signin_existing_user(self, admin):
        user = admin

        self.driver.get(config.BASE_URL)

        page = AuthPage(self.driver)
        page.username = user.login
        page.password = user.password
        page = page.click_login_button()

        assert page.user_is_signin()


@allure.feature('Выход пользователя из системы')
@pytest.mark.usefixtures('wd', 'login')
class TestLogOut(object):
    """Набор тестов выхода пользователя из системы"""

    @allure.story('Выход из системы')
    def test_logout(self):
        self.driver.get(config.BASE_URL)

        page = HomePage(self.driver)
        page = page.nav.click_logout_button()

        assert page.user_is_not_signin()

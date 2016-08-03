# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

from .base import BasePage
from .elements import SimpleInput
from tools.wraps import find_element


class AuthPageLocators(object):
    """Локаторы страницы аутентификации"""

    USERNAME_LOCATOR = (By.ID, 'username')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    LOGIN_BUTTON_LOCATOR = (By.NAME, 'submit')
    LOGIN_FORM_LOCATOR = (By.ID, 'loginform')


class AuthPage(BasePage):
    """Страница аутентификации"""

    username = SimpleInput(AuthPageLocators.USERNAME_LOCATOR)
    password = SimpleInput(AuthPageLocators.PASSWORD_LOCATOR)

    def click_login_button(self):
        elem = find_element(self._driver, AuthPageLocators.LOGIN_BUTTON_LOCATOR)
        elem.click()
        from pages.home import HomePage
        return HomePage(self._driver)

    def user_is_not_signin(self):
        return self._is_element_present(AuthPageLocators.LOGIN_FORM_LOCATOR)

# -*- coding: utf-8 -*-

import allure
from selenium.webdriver.common.by import By

from pages.base import BasePage


class NavBlockLocators(object):
    """Локаторы блока навигации"""

    HOME_LINK_LOCATOR = (By.LINK_TEXT, 'Home')
    MY_PROFILE_LINK_LOCATOR = (By.LINK_TEXT, 'My profile')
    USER_MANAGEMENT_LINK_LOCATOR = (By.LINK_TEXT, 'User management')
    LOG_OUT_LINK_LOCATOR = (By.LINK_TEXT, 'Log out')


class NavBlock(BasePage):
    """Блок навигации"""

    @allure.step('Перейдем на страницу "Home"')
    def go_to_home_page(self):
        self._click(NavBlockLocators.HOME_LINK_LOCATOR)
        from pages.home import HomePage
        return HomePage(self._driver)

    @allure.step('Перейдем на страницу "My profile"')
    def go_to_my_profile_page(self):
        self._click(NavBlockLocators.MY_PROFILE_LINK_LOCATOR)
        # TODO: return My profile page

    @allure.step('Перейдем на страницу "User management"')
    def go_to_user_management_page(self):
        self._click(NavBlockLocators.USER_MANAGEMENT_LINK_LOCATOR)
        # TODO: return User management page

    @allure.step('Нажмем на ссылку "Log out"')
    def click_logout_button(self):
        self._click(NavBlockLocators.LOG_OUT_LINK_LOCATOR)
        self.alert_accept()
        from pages.auth import AuthPage
        return AuthPage(self._driver)

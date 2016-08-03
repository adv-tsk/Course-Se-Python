# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoAlertPresentException, TimeoutException

from tools.wraps import find_element


class BasePage(object):
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self._driver = driver

    def _click(self, locator):
        find_element(self._driver, locator).click()

    def _is_element_present(self, locator):
        try:
            find_element(self._driver, locator)
        except TimeoutException:
            return False
        return True

    def is_alert_present(self):
        try:
            self._driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def alert_text(self):
        return self._driver.switch_to.alert.text

    def alert_accept(self):
        self._driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self._driver.switch_to.alert.dismiss()

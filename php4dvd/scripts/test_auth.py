# -*- coding: utf-8 -*-

import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from conf import config
from tools import browsers


class SignIn(unittest.TestCase):
    """Вход в систему"""

    def setUp(self):
        self.driver = browsers.get_firefox()
        self.driver.implicitly_wait(30)
        self.verification_errors = []
        self.accept_next_alert = True

    def test_input_existing_user(self):
        """
        Проверяем вход в систему с учетными данными
        существующего пользователя
        """
        driver = self.driver
        driver.get(config.BASE_URL)
        self.assertEqual('My movie collection - php4dvd v2.0', driver.title.strip())
        username = driver.find_element_by_id('username')
        username.clear()
        username.send_keys(config.USER)
        password = driver.find_element_by_name('password')
        password.clear()
        password.send_keys(config.PASSWORD)
        driver.find_element_by_name('submit').click()
        self.assertEqual('My movie collection - php4dvd v2.0', driver.title.strip())

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verification_errors)

if __name__ == "__main__":
    unittest.main()

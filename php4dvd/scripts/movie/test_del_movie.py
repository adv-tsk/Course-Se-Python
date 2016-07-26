# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

from conf import config
from tools.wraps import find_element


@allure.feature('Удаление фильма')
@pytest.mark.usefixtures('wd', 'login', 'logout')
class TestDeletingMovie(object):
    """Набор тестов для удаления фильма"""

    @allure.story('Удаление произвольного фильма')
    def test_adding_movie_without_required_fields(self, movie_for_deletion):
        movie = movie_for_deletion

        self.driver.get(config.BASE_URL)
        name = movie.name.encode('utf-8')
        with allure.step('Найдем фильм "{:s}" и нажмем на него левой кнопкой мыши'.format(name)):
            find_element(self.driver, (By.XPATH, '//*[contains(text(), "{:s}")]'.format(name))).click()
        with allure.step('Нажмем на кнопку "Remove"'):
            find_element(self.driver, (By.CSS_SELECTOR, 'img[title="Remove"]')).click()

        assert self.is_alert_present() is True
        assert self.close_alert_and_get_its_text() == 'Are you sure you want to remove this?'
        assert self.movie_present_on_page(movie) is False

    def movie_present_on_page(self, movie):
        name = movie.name.encode('utf-8')
        try:
            find_element(self.driver, (By.CSS_SELECTOR, 'div.movie_cover > div[title="{:s}"]'.format(name)))
        except TimeoutException:
            return False
        return True

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

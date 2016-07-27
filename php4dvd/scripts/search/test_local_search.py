# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from conf import config
from tools.wraps import find_element


@allure.feature('Поиск фильма в локальном каталоге')
@pytest.mark.usefixtures('wd', 'login', 'logout')
class TestLocalSearch(object):
    """Набор тестов для удаления фильма"""

    @allure.story('Поиск существующего и несуществующего фильма')
    def test_search_existing_and_not_existing_movie(self, movie_set_data):
        movie, expect = movie_set_data

        self.driver.get(config.BASE_URL)

        with allure.step('Укажем фильм в строке поиска и нажмем "Enter"'):
            elem = find_element(self.driver, (By.ID, 'q'))
            elem.clear()
            elem.send_keys(movie.name)
            elem.send_keys(Keys.ENTER)
        
        assert self.movie_present_on_page(movie.name.encode('utf-8')) is expect

    def movie_present_on_page(self, name):
        try:
            find_element(self.driver, (By.CSS_SELECTOR, 'div.movie_cover > div[title="{:s}"]'.format(name)))
        except TimeoutException:
            return False
        return True

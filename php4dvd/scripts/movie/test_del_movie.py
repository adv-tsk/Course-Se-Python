# -*- coding: utf-8 -*-

import allure
import pytest

from conf import config
from pages.home import HomePage


@allure.feature('Удаление фильма')
@pytest.mark.usefixtures('wd', 'login', 'logout')
class TestDeletingMovie(object):
    """Набор тестов для удаления фильма"""

    @allure.story('Удаление произвольного фильма')
    def test_removing_movie(self, movie_for_deletion):
        movie = movie_for_deletion

        self.driver.get(config.BASE_URL)
        name = movie.name.encode('utf-8')

        page = HomePage(self.driver)
        page = page.go_to_browse_movie(name)
        page = page.click_remove_button()
        page.search_movie(movie.name)

        assert page.movie_is_not_found()

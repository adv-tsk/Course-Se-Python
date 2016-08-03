# -*- coding: utf-8 -*-

import allure
import pytest

from pages.home import HomePage


@allure.feature('Поиск фильма в локальном каталоге')
@pytest.mark.usefixtures('wd', 'login', 'logout')
class TestLocalSearch(object):
    """Набор тестов для удаления фильма"""

    @allure.story('Поиск существующего фильма')
    def test_search_existing_movie(self, movie_exists):
        movie = movie_exists

        page = HomePage(self.driver)
        page.search_movie(movie.name)

        assert page.movie_is_found(movie.name.encode('utf-8'))

    @allure.story('Поиск несуществующего фильма')
    def test_search_not_existing_movie(self, movie_not_exists):
        movie = movie_not_exists

        page = HomePage(self.driver)
        page.search_movie(movie.name)

        assert page.movie_is_not_found()

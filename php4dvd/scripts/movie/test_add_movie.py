# -*- coding: utf-8 -*-

import allure
import pytest

from conf import config
from pages.home import HomePage


@allure.feature('Создание описания фильма')
@pytest.mark.usefixtures('wd', 'login', 'logout')
class TestAddingMovie(object):
    """Набор тестов создания описания фильма"""

    @allure.story('Создание описания фильма без заполнения обязательного поля "Title"')
    def test_adding_movie_without_required_title_field(self, movie_with_wrong_data):
        movie = movie_with_wrong_data

        self.driver.get(config.BASE_URL)

        page = HomePage(self.driver)
        page = page.click_add_movie_button()
        page.year = movie.year
        page.click_save_button()

        assert page.title_field_is_required_present()

    @allure.story('Создание описания фильма без заполнения обязательного поля "Year"')
    def test_adding_movie_without_required_year_field(self, movie_with_wrong_data):
        movie = movie_with_wrong_data

        self.driver.get(config.BASE_URL)

        page = HomePage(self.driver)
        page = page.click_add_movie_button()
        page.title = movie.name
        page.click_save_button()

        assert page.year_field_is_required_present()

    @allure.story('Создание описания фильма со всеми обязательными полями')
    def test_adding_movie_with_all_required_fields(self, movie_with_only_required_fields):
        movie = movie_with_only_required_fields

        self.driver.get(config.BASE_URL)

        page = HomePage(self.driver)
        page = page.click_add_movie_button()
        page.title = movie.name
        page.year = movie.year
        page = page.click_save_button()

        assert page.title == u'{:s} ({:d})'.format(movie.name, movie.year)
    
    @allure.story('Создание описания фильма с заполнением обязательных и доп. полей')
    def test_adding_movie_with_required_and_additional_fields(self, movie_with_additional_fields):
        movie = movie_with_additional_fields

        self.driver.get(config.BASE_URL)

        page = HomePage(self.driver)
        page = page.click_add_movie_button()
        page.title = movie.name
        page.also_know_as = movie.original_name
        page.year = movie.year
        page.duration = movie.duration
        page.trailer_url = movie.trailer
        page.format = movie.format
        page.country = movie.country
        page.director = movie.director
        page.writer = movie.writer
        page.producer = movie.producer
        page = page.click_save_button()

        assert page.title == u'{:s} ({:d})'.format(movie.name, movie.year)

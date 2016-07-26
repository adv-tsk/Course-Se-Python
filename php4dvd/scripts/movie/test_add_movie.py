# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from conf import config
from tools.wraps import find_element


@allure.feature('Создание описания фильма')
@pytest.mark.usefixtures('wd', 'login', 'logout')
class TestAddingMovie(object):
    """Набор тестов создания описания фильма"""

    @allure.story('Создание описания фильма без заполнения обязательных полей')
    def test_adding_movie_without_required_fields(self, movie_with_wrong_data):
        movie = movie_with_wrong_data

        self.driver.get(config.BASE_URL)
        self.got_to_add_movie()
        self.type_name(movie.name)
        self.click_save_button()

        assert self.year_field_is_required_present() is True

    @allure.story('Создание описания фильма со всеми обязательными полями')
    def test_adding_movie_with_all_required_fields(self, movie_with_only_required_fields):
        movie = movie_with_only_required_fields

        self.driver.get(config.BASE_URL)
        self.got_to_add_movie()
        self.type_name(movie.name)
        self.type_year(movie.year)
        self.click_save_button()

        assert self.get_title_movie() == u'{:s} ({:d})'.format(movie.name, movie.year)

    @allure.story('Создание описания фильма с заполнением обязательных и доп. полей')
    def test_adding_movie_with_required_and_additional_fields(self, movie_with_additional_fields):
        movie = movie_with_additional_fields

        self.driver.get(config.BASE_URL)
        self.got_to_add_movie()
        self.type_name(movie.name)
        self.type_original_name(movie.original_name)
        self.type_year(movie.year)
        self.type_duration(movie.duration)
        self.type_trailer(movie.trailer)
        self.type_format(movie.format)
        self.type_country(movie.country)
        self.type_director(movie.director)
        self.type_writer(movie.writer)
        self.type_producer(movie.producer)
        self.click_save_button()

        assert self.get_title_movie() == u'{:s} ({:d})'.format(movie.name, movie.year)

    def year_field_is_required_present(self):
        try:
            find_element(self.driver, (By.CSS_SELECTOR, 'input[name="year"].error'))
        except TimeoutException:
            return False
        return True

    def get_title_movie(self):
        return find_element(self.driver, (By.ID, 'movie')).find_element(By.TAG_NAME, 'h2').text

    def got_to_add_movie(self):
        with allure.step('Нажимаем на кнопку "Add movie"'):
            find_element(self.driver, (By.CSS_SELECTOR, 'img[title="Add movie"]')).click()

    def click_save_button(self):
        with allure.step('Нажимаем на кнопку "Save"'):
            find_element(self.driver, (By.ID, 'submit')).click()

    def type_name(self, value):
        with allure.step('Укажем заголовок фильма'):
            find_element(self.driver, (By.NAME, 'name')).send_keys(value)

    def type_original_name(self, value):
        with allure.step('Укажем оригинальное название фильма'):
            find_element(self.driver, (By.NAME, 'aka')).send_keys(value)

    def type_year(self, value):
        with allure.step('Укажем год'):
            find_element(self.driver, (By.NAME, 'year')).send_keys(value)

    def type_duration(self, value):
        with allure.step('Укажем продолжительность фильма'):
            find_element(self.driver, (By.NAME, 'duration')).send_keys(value)

    def type_trailer(self, value):
        with allure.step('Укажем URL трейлера'):
            find_element(self.driver, (By.NAME, 'trailer')).send_keys(value)

    def type_format(self, value):
        with allure.step('Укажем формат фильма'):
            elem = find_element(self.driver, (By.NAME, 'format'))
            elem.clear()
            elem.send_keys(value)

    def type_country(self, value):
        with allure.step('Укажем страну'):
            find_element(self.driver, (By.NAME, 'country')).send_keys(value)

    def type_director(self, value):
        with allure.step('Укажем режиссера'):
            find_element(self.driver, (By.NAME, 'director')).send_keys(value)

    def type_writer(self, value):
        with allure.step('Укажем сценариста'):
            find_element(self.driver, (By.NAME, 'writer')).send_keys(value)

    def type_producer(self, value):
        with allure.step('Укажем продюсера'):
            find_element(self.driver, (By.NAME, 'producer')).send_keys(value)

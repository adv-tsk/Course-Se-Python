# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest
from pages.home import HomePage


@pytest.fixture
def movie_with_wrong_data():
    class Movie(object):
        name = 'Охотники за приведениями'
        year = 1979
    return Movie


@pytest.fixture
def movie_with_only_required_fields():
    class Movie(object):
        name = 'Доктор Стрэндж'
        year = 2016
    return Movie


@pytest.fixture
def movie_with_additional_fields():
    class Movie(object):
        name = 'Тайная жизнь домашних животных'
        original_name = 'The Secret Life of Pets'
        year = 2016
        duration = '87'
        format = 'Blu-ray'
        trailer = 'http://www.kinopoisk.ru/getlink.php?id=309084&type=trailer&link=' \
                  'https://kp.cdn.yandex.net/743088/kinopoisk.ru-Secret-Life-of-Pets_-The-309084.mp4'
        country = 'Япония, США'
        director = 'Ярроу Чейни, Крис Рено'
        writer = 'Синко Пол, Кен Даурио, Брайан Линч'
        producer = 'Джанет Хили, Бретт Хоффман, Кристофер Меледандри'
    return Movie


@pytest.fixture
def movie_for_deletion(driver):
    class Movie(object):
        name = 'Парни со стволами'
        year = 2016
    # для начала создадим фильм, который потом будем удалять
    page = HomePage(driver)
    page = page.click_add_movie_button()
    page.title = Movie.name
    page.year = Movie.year
    page.click_save_button()
    return Movie

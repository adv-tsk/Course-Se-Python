# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest


@pytest.fixture
def movie_exists():
    class Movie(object):
        name = 'Ураган'
        year = 2018
    return Movie


@pytest.fixture
def movie_not_exists():
    class Movie(object):
        name = 'XXX'
        year = 1970
    return Movie

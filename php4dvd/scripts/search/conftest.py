# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest


class MovieExists(object):
    name = 'Ураган'
    year = 2018


class MovieNotExists(object):
    name = 'XXX'
    year = 1970


@pytest.fixture(scope='function', params=[
    (MovieExists, True),
    (MovieNotExists, False),
])
def movie_set_data(request):
    return request.param

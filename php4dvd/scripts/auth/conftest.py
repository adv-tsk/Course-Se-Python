# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def user_not_exists():
    class User(object):
        login = 'anonymous'
        password = 'hackyoursite'
    return User

# -*- coding: utf-8 -*-

from tools.wraps import find_element


class SimpleInput(object):
    """Класс для элемента <input/> разметки html"""

    def __init__(self, locator, read_only=False):
        self.locator = locator
        self.read_only = read_only

    def __set__(self, obj, value):
        """Устанавливает значение для элемента"""
        if not self.read_only:
            element = find_element(obj._driver, self.locator)
            element.clear()
            element.send_keys(value)

    def __get__(self, obj, owner):
        """Получает значение элемента"""
        element = find_element(obj._driver, self.locator)
        return element.get_attribute('value')


class SimpleText(object):
    """Класс представляющий собой текст любого элемента"""

    def __init__(self, locator):
        self.locator = locator

    def __get__(self, obj, owner):
        """Получает значение элемента"""
        element = find_element(obj._driver, self.locator)
        return element.text

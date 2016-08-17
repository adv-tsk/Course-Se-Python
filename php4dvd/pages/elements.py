# -*- coding: utf-8 -*-

import allure
from selenium.common.exceptions import NoSuchElementException, UnexpectedTagNameException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from tools.wraps import find_element
from tools import browsers


class SimpleInput(object):
    """Класс для элемента <input/> разметки html"""

    def __init__(self, locator, text=None, read_only=False):
        self.locator = locator
        self.read_only = read_only
        if text:
            self.set = allure.step('Введем ' + text)(self.set)

    def set(self, obj, value):
        element = find_element(obj._driver, self.locator)
        element.clear()
        element.send_keys(value)

    def __set__(self, obj, value):
        """Устанавливает значение для элемента"""
        if self.read_only:
            raise ValueError('Can not be set a value at a read only element')
        return self.set(obj, value)

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


#############################################################################

def actions():
    return ActionChains(browsers.get_webdriver())


def hover(element):
    """
    Определяет стиль элемента при наведении на него
    курсора мыши (псевдокласс :hover)

    :type element: selenium.webdriver.remote.webelement.WebElement
    :rtype: selenium.webdriver.remote.webelement.WebElement
    """
    el = actions().move_to_element(element)
    el.perform()
    return element


class RootElement(object):
    def __getattr__(self, item):
        return getattr(browsers.get_webdriver(), item)


class Select(object):
    """Представляет собой элемент интерфейса в виде раскрывающегося списка"""

    def __init__(self, locator, context=None):
        """
        :type context: selenium.webdriver.remote.webelement.WebElement | selenium.webdriver.remote.webdriver.WebDriver
        """
        self._driver = RootElement()
        self._context = context or self._driver
        self._el = self._context.find_element(*locator)

        if self._el.tag_name.lower() != 'table' or \
           self._el.get_attribute('cmptype') != 'ComboBox':
            raise UnexpectedTagNameException('Select only works on <table[cmptype="ComboBox"]> elements')

    def _set_selected(self, option):
        """
        Выбирает данную опцию

        :type option: selenium.webdriver.remote.webelement.WebElement
        """
        # TODO: в geckodriver move_to_element пока не реализован
        # hover(option).click()
        option.click()

    @staticmethod
    def _normalize_string(value):
        """
        Приводит строку к сравниваемому виду

        :type value: unicode
        :rtype: unicode
        """
        replace = ('&nbsp;', ' ', '\n', '\t')
        for char in replace:
            value = value.replace(char, '')
        return value.lower()

    @property
    def options(self):
        """
        Возвращает список всех опций

        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        """
        css = 'body > div.combo-box-drop-list:last-child tr[cmptype="ComboItem"]'
        return self._driver.find_elements(By.CSS_SELECTOR, css)

    def select_by_index(self, index):
        """
        Выбор опции по индексу

        :param index: Индекс опции, которая будет выбрана
        :type index: int
        """
        self._el.click()
        match = str(index)
        for opt in self.options:
            if opt.get_attribute('index') == match and \
               opt.is_displayed():
                self._set_selected(opt)
                break
        else:
            raise NoSuchElementException('Не удалось найти видимый элемент с индексом: {:d}'.format(index))

    def select_by_value(self, value):
        """
        Выбор опции по значению (атрибут "value")

        :param value: Значение для сопоставления
        :type value: unicode
        """
        self._el.click()
        value = self._normalize_string(value)
        for opt in self.options:
            val = opt.get_attribute('value')
            if self._normalize_string(val) == value and \
               opt.is_displayed():
                self._set_selected(opt)
                break
        else:
            raise NoSuchElementException('Не удалось найти видимый элемент со значением: {:s}'.format(value))

    def select_by_visible_text(self, text):
        """
        Выбор опции по видимому тексту

        :param text: Значение для сопоставления
        :type text: unicode
        """
        self._el.click()
        txt = self._normalize_string(text)
        for opt in self.options:
            td = opt.find_element(By.CSS_SELECTOR, 'td')
            if txt in self._normalize_string(td.text) and \
               opt.is_displayed():
                self._set_selected(td)
                break
        else:
            raise NoSuchElementException('Не удалось найти видимый элемент с текстом: {:s}'.format(text))

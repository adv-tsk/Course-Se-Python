# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


def find_element(driver, element_locator):
    """
    Поиск элемента
    :type driver: selenium.webdriver.Firefox
    :type element_locator: tuple
    """
    WebDriverWait(driver, 3).until(visibility_of_element_located(element_locator))
    element = driver.find_element(*element_locator)
    return element


# -*- coding: utf-8 -*-

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


def find_element(driver, element_locator):
    """
    Поиск элемента
    :type driver: selenium.webdriver.Firefox
    :type element_locator: tuple
    :rtype: selenium.webdriver.remote.webelement.WebElement
    """
    time.sleep(.2)
    WebDriverWait(driver, 3).until(visibility_of_element_located(element_locator))
    element = driver.find_element(*element_locator)
    return element

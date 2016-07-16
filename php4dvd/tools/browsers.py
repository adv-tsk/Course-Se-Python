# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from conf import browsers


def get_firefox():
    """
    Возвращает драйвер браузера Firefox
    :rtype: webdriver.Firefox
    """
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    firefox_capabilities['binary'] = browsers.FIREFOX['binary']

    driver = webdriver.Firefox(capabilities=firefox_capabilities,
                               executable_path=browsers.FIREFOX['executable_path'])
    return driver


def get_chrome():
    """
    Возвращает драйвер браузера Google Chrome
    :rtype: webdriver.Chrome
    """
    return webdriver.Chrome()


def get_ie():
    """
    Возвращает драйвер браузера Internet Explorer
    :rtype: webdriver.Ie
    """
    return webdriver.Ie()

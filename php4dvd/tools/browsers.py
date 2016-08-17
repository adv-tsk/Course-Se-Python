# -*- coding: utf-8 -*-

import threading

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from conf import browsers


_local = threading.local()


def get_firefox(remote=False, selenium_hub=None):
    """
    Возвращает драйвер браузера Firefox
    :rtype: webdriver.Firefox
    """
    if remote:
        driver = webdriver.Remote(
            command_executor=selenium_hub,
            desired_capabilities=DesiredCapabilities.FIREFOX,
        )
    else:
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        firefox_capabilities['binary'] = browsers.FIREFOX['binary']

        driver = webdriver.Firefox(capabilities=firefox_capabilities,
                                   executable_path=browsers.FIREFOX['executable_path'])
    return driver


def get_chrome(remote, selenium_hub):
    """
    Возвращает драйвер браузера Google Chrome
    :rtype: webdriver.Chrome
    """
    raise NotImplementedError()


def get_ie(remote, selenium_hub):
    """
    Возвращает драйвер браузера Internet Explorer
    :rtype: webdriver.Ie
    """
    raise NotImplementedError()


def set_webdriver(driver):
    _local.webdriver = driver


def get_webdriver():
    return _local.webdriver


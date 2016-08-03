# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import BasePage
from .blocks.nav import NavBlock
from tools.wraps import find_element


class HomePageLocators(object):
    """Локаторы стартовой страницы"""

    ADD_MOVIE_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'img[title="Add movie"]')
    UPDATE_ALL_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'img[title="Update all"]')
    EXPORT_ALL_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'Export')
    SEARCH_MOVIE_LOCATOR = (By.ID, 'q')
    NAV_PANEL_LOCATOR = (By.TAG_NAME, 'nav')
    MOVIE_LOCATOR = (By.CSS_SELECTOR, 'div.movie_cover > div[title="{:s}"]')
    NOT_FOUND_MESSAGE_LOCATOR = (By.CSS_SELECTOR, '#results div.content')
    NOT_FOUND_MESSAGE_CONTENT = u'No movies where found.'


class HomePage(BasePage):
    """Стартовая страница"""

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.nav = NavBlock(driver)

    def click_add_movie_button(self):
        """
        :rtype: AddMoviePage
        """
        self._click(HomePageLocators.ADD_MOVIE_BUTTON_LOCATOR)
        from .movie import AddMoviePage
        return AddMoviePage(self._driver)

    def click_update_all_button(self):
        """
        :rtype: HomePage
        """
        self._click(HomePageLocators.UPDATE_ALL_BUTTON_LOCATOR)
        return self

    def click_export_all_button(self):
        self._click(HomePageLocators.EXPORT_ALL_BUTTON_LOCATOR)

    def search_movie(self, value):
        """
        :type value: unicode
        """
        elem = find_element(self._driver, HomePageLocators.SEARCH_MOVIE_LOCATOR)
        elem.clear()
        elem.send_keys(value)
        elem.send_keys(Keys.ENTER)

    def movie_is_found(self, value):
        """
        :rtype: bool
        """
        t, l = HomePageLocators.MOVIE_LOCATOR
        locator = (t, l.format(value))
        return self._is_element_present(locator)

    def movie_is_not_found(self):
        elem = find_element(self._driver, HomePageLocators.NOT_FOUND_MESSAGE_LOCATOR)
        return elem.text == HomePageLocators.NOT_FOUND_MESSAGE_CONTENT

    def go_to_browse_movie(self, value):
        """
        :rtype: BrowseMoviePage
        """
        t, l = HomePageLocators.MOVIE_LOCATOR
        locator = (t, l.format(value))
        self._click(locator)
        from pages.movie import BrowseMoviePage
        return BrowseMoviePage(self._driver)

    def user_is_signin(self):
        """
        :rtype: bool
        """
        return self._is_element_present(HomePageLocators.NAV_PANEL_LOCATOR)

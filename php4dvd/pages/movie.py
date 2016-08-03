# -*- coding: utf-8 -*-

import allure
from selenium.webdriver.common.by import By

from .base import BasePage
from .elements import SimpleInput, SimpleText
from .blocks.nav import NavBlock


class BrowseMoviePageLocators(object):
    """Локаторы страницы просмотра информации о фильме"""

    TITLE_LOCATOR = (By.CSS_SELECTOR, '#movie h2')
    COUNTRY_LOCATOR = (By.NAME, 'country')
    DIRECTOR_LOCATOR = (By.NAME, 'director')
    WRITER_LOCATOR = (By.NAME, 'writer')
    PRODUCER_LOCATOR = (By.NAME, 'producer')
    EDIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'img[title="Edit"]')
    REMOVE_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'img[title="Remove"]')


class BrowseMoviePage(BasePage):
    """Страница просмотра информации о фильме"""

    def __init__(self, driver):
        super(BrowseMoviePage, self).__init__(driver)
        self.nav = NavBlock(driver)

    title = SimpleText(BrowseMoviePageLocators.TITLE_LOCATOR)
    director = SimpleText(BrowseMoviePageLocators.DIRECTOR_LOCATOR)
    writer = SimpleText(BrowseMoviePageLocators.WRITER_LOCATOR)
    producer = SimpleText(BrowseMoviePageLocators.PRODUCER_LOCATOR)

    @allure.step('Нажмем на кноку "Edit"')
    def click_edit_button(self):
        """
        :rtype: EditMoviePage
        """
        self._click(BrowseMoviePageLocators.EDIT_BUTTON_LOCATOR)
        return EditMoviePage(self._driver)

    @allure.step('Нажмем на кноку "Remove"')
    def click_remove_button(self):
        """
        :rtype: HomePage
        """
        self._click(BrowseMoviePageLocators.REMOVE_BUTTON_LOCATOR)
        self.alert_accept()
        from .home import HomePage
        return HomePage(self._driver)


class AddMoviePageLocators(object):
    """Локаторы страницы создания описания фильма"""

    TITLE_INPUT_LOCATOR = (By.NAME, 'name')
    TITLE_INPUT_ERROR_LOCATOR = (By.CSS_SELECTOR, 'input[name="name"].error')
    ALSO_KNOWN_AS_INPUT_LOCATOR = (By.NAME, 'aka')
    YEAR_INPUT_LOCATOR = (By.NAME, 'year')
    YEAR_INPUT_ERROR_LOCATOR = (By.CSS_SELECTOR, 'input[name="year"].error')
    DURATION_INPUT_LOCATOR = (By.NAME, 'duration')
    TRAILER_URL_INPUT_LOCATOR = (By.NAME, 'trailer')
    FORMAT_INPUT_LOCATOR = (By.NAME, 'format')
    COUNTRY_INPUT_LOCATOR = (By.NAME, 'country')
    DIRECTOR_INPUT_LOCATOR = (By.NAME, 'director')
    WRITER_INPUT_LOCATOR = (By.NAME, 'writer')
    PRODUCER_INPUT_LOCATOR = (By.NAME, 'producer')
    SAVE_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'img[title="Save"]')


class AddMoviePage(BasePage):
    """Страница создания описания фильма"""

    def __init__(self, driver):
        super(AddMoviePage, self).__init__(driver)
        self.nav = NavBlock(driver)

    title = SimpleInput(AddMoviePageLocators.TITLE_INPUT_LOCATOR, 'название фильма')
    also_know_as = SimpleInput(AddMoviePageLocators.ALSO_KNOWN_AS_INPUT_LOCATOR, 'оригинальное название фильма')
    year = SimpleInput(AddMoviePageLocators.YEAR_INPUT_LOCATOR, 'год')
    duration = SimpleInput(AddMoviePageLocators.DURATION_INPUT_LOCATOR, 'продолжительность')
    trailer_url = SimpleInput(AddMoviePageLocators.TRAILER_URL_INPUT_LOCATOR, 'адрес трейлера')
    format = SimpleInput(AddMoviePageLocators.FORMAT_INPUT_LOCATOR, 'формат')
    country = SimpleInput(AddMoviePageLocators.COUNTRY_INPUT_LOCATOR, 'страну')
    director = SimpleInput(AddMoviePageLocators.DIRECTOR_INPUT_LOCATOR, 'директора')
    writer = SimpleInput(AddMoviePageLocators.WRITER_INPUT_LOCATOR, 'сценариста')
    producer = SimpleInput(AddMoviePageLocators.PRODUCER_INPUT_LOCATOR, 'продюсера')

    @allure.step('Нажмем на кноку "Save"')
    def click_save_button(self):
        """
        :rtype: BrowseMoviePage
        """
        self._click(AddMoviePageLocators.SAVE_BUTTON_LOCATOR)
        return BrowseMoviePage(self._driver)

    def title_field_is_required_present(self):
        """
        :rtype: bool
        """
        return self._is_element_present(AddMoviePageLocators.TITLE_INPUT_ERROR_LOCATOR)

    def year_field_is_required_present(self):
        """
        :rtype: bool
        """
        return self._is_element_present(AddMoviePageLocators.YEAR_INPUT_ERROR_LOCATOR)


class EditMoviePageLocators(object):
    """Локаторы для страницы редактирования описания фильма"""

    REMOVE_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'img[title="Remove"]')


class EditMoviePage(AddMoviePage):
    """Страница редактирования описания фильма"""

    @allure.step('Нажмем на кноку "Remove"')
    def click_remove_button(self):
        """
        :rtype: HomePage
        """
        self._click(EditMoviePageLocators.REMOVE_BUTTON_LOCATOR)
        self.alert_accept()
        from .home import HomePage
        return HomePage(self._driver)

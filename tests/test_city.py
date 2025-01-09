import allure
from allure_commons.types import LabelType

from pages.main_page import MainPage


@allure.epic("Helix")
@allure.feature("Город")
class TestCity:
    @allure.story("Смена города")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("NORMAL")
    def test_change_city(self, browser_driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage()
            main_page.open_page_with_confirm("")
        with allure.step("Изменить город"):
            main_page.change_city()
        with allure.step("Проверить текущий город"):
            main_page.check_current_city("Москва")

    @allure.story("Отказ от города по умолчанию")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("NORMAL")
    def test_reject_city(self, browser_driver):
        with allure.step("Открыть главную страницу с отказом от города"):
            main_page = MainPage()
            main_page.open_page_with_reject("")
        with allure.step("Выбрать город"):
            main_page.choose_city()
        with allure.step("Проверить текущий город"):
            main_page.check_current_city("Москва")

    @allure.story("Выбор города по умолчанию")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_confirm_city(self, browser_driver):
        with allure.step("Открыть главную страницу с выбором города по умолчанию"):
            main_page = MainPage()
            main_page.open_page_with_confirm("")
        with allure.step("Проверить текущий город"):
            main_page.check_current_city("Санкт-Петербург")

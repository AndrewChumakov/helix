import allure
from allure_commons.types import LabelType

from pages.main_page import MainPage


@allure.epic("Helix")
@allure.feature("Поиск")
class TestSearch:
    @allure.story("Поиск на сайте")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("CRITICAL")
    def test_search(self, browser_driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage()
            main_page.open_page_with_confirm("")
        with allure.step("Найти на сайте"):
            main_page.search("ЭЛИ")
        with allure.step("Проверить результаты поиска"):
            main_page.check_count(5)
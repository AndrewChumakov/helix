import allure
from allure_commons.types import LabelType

from pages.main_page import MainPage


@allure.epic("HELIX")
@allure.feature("Навигация")
class TestNavigation:
    @allure.story("Наличие вкладки 'Скидки и акции' в хедере")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("NORMAL")
    def test_promo_from_header(self, browser_driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage()
            main_page.open_page_with_confirm("")
        with allure.step("Проверить наличие вкладки 'Скидки и акции'"):
            main_page.check_promo_from_header()

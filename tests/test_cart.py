import allure
from allure_commons.types import LabelType

from pages.cart_page import CartPage
from pages.main_page import MainPage


@allure.epic("Helix")
@allure.feature("Корзина")
class TestCart:
    @allure.story("Добавление в корзину")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("BLOCKER")
    def test_add_to_cart(self, browser_driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage()
            main_page.open_page_with_confirm("")
        with allure.step("Найти на сайте"):
            main_page.search("ЭЛИ")
        with allure.step("Добавить в корзину"):
            main_page.add_to_cart()
        with allure.step("Открыть корзину"):
            main_page.open_cart()
        with allure.step("Проверить наличие добавленного исследования"):
            cart_page = CartPage()
            cart_page.check_item("ЭЛИ-Н-ТЕСТ")

    @allure.story("Удаление из корзины")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("CRITICAL")
    def test_delete_from_cart(self, browser_driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage()
            main_page.open_page_with_confirm("")
        with allure.step("Найти на сайте"):
            main_page.search("ЭЛИ")
        with allure.step("Добавить в корзину"):
            main_page.add_to_cart()
        with allure.step("Открыть корзину"):
            main_page.open_cart()
        with allure.step("Удалить исследование"):
            cart_page = CartPage()
            cart_page.delete_from_cart()
            cart_page.confirm_delete()
        with allure.step("Проверить, что корзина пустая"):
            cart_page.check_empty_cart()

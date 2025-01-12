import allure
from allure_commons.types import LabelType

from data.cart import CartText
from data.models import eli
from pages.cart_page import cart_page
from pages.main_page import main_page


@allure.epic("Helix")
@allure.feature("Корзина")
@allure.label(LabelType.TAG, "smoke")
class TestCart:
    @allure.story("Добавление в корзину")
    @allure.severity("BLOCKER")
    def test_add_to_cart(self):
        main_page.open_page("", True)
        main_page.search_item(eli.short_name)
        main_page.add_to_cart()
        main_page.open_cart()
        cart_page.check_item_exist(eli.full_name)

    @allure.story("Удаление из корзины")
    @allure.severity("CRITICAL")
    def test_delete_from_cart(self):
        main_page.open_page("", True)
        main_page.search_item(eli.short_name)
        main_page.add_to_cart()
        main_page.open_cart()
        cart_page.delete_from_cart(True)
        cart_page.check_empty_cart_text(CartText.EmptyCart)

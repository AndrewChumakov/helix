import allure
from allure_commons.types import LabelType

from data.header import HeaderName
from pages.main_page import main_page


@allure.epic("Helix")
@allure.feature("Навигация")
class TestNavigation:
    @allure.story("Наличие вкладки со скидками в хедере")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("NORMAL")
    def test_promo_from_header(self):
        main_page.open_page("", True)
        main_page.check_promo_text_from_header(HeaderName.PROMO)

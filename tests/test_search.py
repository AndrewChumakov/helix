import allure
from allure_commons.types import LabelType

from data.models import eli
from pages.main_page import main_page


@allure.epic("Helix")
@allure.feature("Поиск")
class TestSearch:
    @allure.story("Поиск на сайте")
    @allure.label(LabelType.TAG, "smoke")
    @allure.severity("CRITICAL")
    def test_search(self):
        main_page.open_page("", True)
        main_page.search_item(eli.short_name)
        main_page.check_count(eli.count)

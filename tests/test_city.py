import allure
from allure_commons.types import LabelType

from data.city import CityName
from pages.main_page import main_page


@allure.epic("Helix")
@allure.feature("Город")
@allure.label(LabelType.TAG, "smoke")
class TestCity:
    @allure.story("Смена города")
    @allure.severity("NORMAL")
    def test_change_city(self):
        main_page.open_page("", True)
        main_page.change_city()
        main_page.check_current_city(CityName.MOSCOW)

    @allure.story("Отказ от города по умолчанию")
    @allure.severity("NORMAL")
    def test_reject_city(self):
        main_page.open_page("", False)
        main_page.choose_city()
        main_page.check_current_city(CityName.MOSCOW)

    @allure.story("Выбор города по умолчанию")
    @allure.severity("BLOCKER")
    def test_confirm_city(self):
        main_page.open_page("", True)
        main_page.check_current_city(CityName.DEFAULT_CITY)

import allure
from selene import browser, have


class MainPage:

    def __init__(self):
        self.promo_header = browser.element("//a[@data-testid='header-nav-promo']")
        self.confirm_city = browser.element("//button[@data-testid='confirm-city-button']")
        self.reject_city = browser.element("//button[@data-testid='reject-city-button']")
        self.city = browser.element("//span[@data-testid='important-city-0']")
        self.current_city = browser.element("//span[@data-testid='current-city']")
        self.catalog = browser.element("//a[@data-testid='header-nav-catalog']")
        self.search_bar = browser.element("//input[@data-testid='search-placeholder']")
        self.count = browser.element("//div[@class ='typography typography-paragraph typography-body grey-300']")
        self.add = browser.all("//button[@class='button button-primary button-xs full-width ng-star-inserted']")
        self.cart = browser.element("//span[@data-testid='header-nav-cart-button']")

    @allure.step("Открыть главную страницу")
    def open_page(self, page, confirm):
        browser.open(page)
        if confirm:
            self.confirm_city.click()
        else:
            self.reject_city.click()

    @allure.step("Проверить наличие вкладки со скидками")
    def check_promo_text_from_header(self, promo_text):
        self.promo_header.should(have.text(promo_text))

    @allure.step("Изменить город")
    def change_city(self):
        self.current_city.click()
        self.choose_city()

    @allure.step("Проверить текущий город")
    def check_current_city(self, city):
        self.current_city.should(have.text(city))

    @allure.step("Выбрать город")
    def choose_city(self):
        self.city.click()

    @allure.step("Найти на сайте")
    def search_item(self, item):
        self.search_bar.type(item)

    @allure.step("Проверить количество результатов поиска")
    def check_count(self, count):
        self.count.should(have.text("Количество результатов: " + str(count)))

    @allure.step("Добавить в корзину")
    def add_to_cart(self):
        self.add.first.click()

    @allure.step("Открыть корзину")
    def open_cart(self):
        self.cart.click()


main_page = MainPage()

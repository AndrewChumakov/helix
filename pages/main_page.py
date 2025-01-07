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


    def open_page(self, page):
        browser.open(page)

    def open_page_with_confirm(self, page):
        self.open_page(page)
        self.confirm_city.click()

    def open_page_with_reject(self, page):
        self.open_page(page)
        self.reject_city.click()

    def check_promo_from_header(self):
        self.promo_header.should(have.text("Скидки и акции"))

    def change_city(self):
        self.current_city.click()
        self.choose_city()

    def check_current_city(self, city):
        self.current_city.should(have.text(city))

    def choose_city(self):
        self.city.click()

    def search(self, item):
        self.search_bar.type(item)

    def check_count(self, count):
        self.count.should(have.text("Количество результатов: " + str(count)))

    def add_to_cart(self):
        self.add.first.click()

    def open_cart(self):
        self.cart.click()
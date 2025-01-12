import allure
from selene import browser, have


class CartPage:
    def __init__(self):
        self.cart_items = browser.all("//a[@data-testid='cart-item-title-link']")
        self.delete = browser.all("//button[@data-testid='analyse-delete-button']")
        self.confirm = browser.element("//button[@data-testid='confirmation-button']")
        self.reject = browser.element("//button[@data-testid='rejection-button']")
        self.cart = browser.element(
            "//h1[@class='typography typography-h1 typography-paragraph grey-900 ng-star-inserted']")

    @allure.step("Проверить наличие добавленного исследования")
    def check_item_exist(self, item):
        self.cart_items.first.should(have.text(item))

    @allure.step("Удалить исследование")
    def delete_from_cart(self, confirm):
        self.delete.first.click()
        if confirm:
            self.confirm.click()
        else:
            self.reject.click()

    @allure.step("Проверить, что корзина пустая")
    def check_empty_cart_text(self, text):
        self.cart.should(have.text(text))


cart_page = CartPage()

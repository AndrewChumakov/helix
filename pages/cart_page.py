from selene import browser, have


class CartPage:
    def __init__(self):
        self.cart_items = browser.all("//a[@data-testid='cart-item-title-link']")
        self.delete = browser.all("//button[@data-testid='analyse-delete-button']")
        self.confirm = browser.element("//button[@data-testid='confirmation-button']")
        self.cart = browser.element("//h1[@class='typography typography-h1 typography-paragraph grey-900 ng-star-inserted']")

    def check_item(self, item):
        self.cart_items.first.should(have.text(item))

    def delete_from_cart(self):
        self.delete.first.click()

    def confirm_delete(self):
        self.confirm.click()

    def check_empty_cart(self):
        self.cart.should(have.text("Корзина заказов пуста"))
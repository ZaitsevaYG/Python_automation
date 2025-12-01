from playwright.sync_api import Page, expect
from utils import close_promo_popup
from data.books import Book



class CartPage:
    def __init__(self, page: Page, book: Book):
        self.page = page
        self.book = book
        self.add_to_cart_btn = page.get_by_test_id("book__addToCartButton")
        self.already_in_the_cart_btn = page.get_by_test_id("book__goToCartButton")
        self.delete_btn = page.get_by_test_id("cart__listDeleteButton")
        self.delete_popup = page.get_by_test_id("cart__modalDeleteArtp")
        self.delete_and_postpone_btn = page.get_by_role("button", name="Отложить и удалить")
        self.empty_heart_icon = page.get_by_role("button", name="Отложить").get_by_test_id("icon_favorites")
        self.filled_heart_icon = page.get_by_role("button", name="В отложенном").get_by_test_id("icon_favoritesFilled")
        self.delete_from_cart_popup_btn = page.get_by_test_id("cart__modalDeleteArt").get_by_role("button", name="Удалить")
        self.checkout_btn = page.get_by_role("button", name="Перейти к покупке")
        self.checkout_total = page.get_by_test_id("cart__checkout--total")
        self.empty_cart_state = page.get_by_test_id("cart__emptyState--wrapper")


    def get_book_locator(self):

        if not self.book.id:
            raise ValueError("Book ID is required to locate item in cart")
        return self.page.get_by_test_id(f"cart__listItem--{self.book.id}")


    def navigate_and_add_to_cart(self):
        self.page.goto(self.book.url, wait_until='domcontentloaded')
        book_title = self.page.get_by_role("heading", name=self.book.title)
        book_title.wait_for(state="visible")
        self.add_to_cart_btn.click()

        close_promo_popup(self.page)

        self.already_in_the_cart_btn.is_visible(timeout=1000)
        self.already_in_the_cart_btn.click()
        self.page.wait_for_timeout(timeout=1000)

    def postpone_book(self):
        book_in_cart = self.get_book_locator()
        book_in_cart.get_by_role("button", name="Отложить").click()
        return self


    def delete_from_cart_and_postpone (self):
        expect(self.empty_heart_icon).to_be_visible()
        self.delete_btn.click()
        expect(self.delete_popup).to_be_visible()
        self.delete_and_postpone_btn.click()
        return self


    def delete_from_cart (self):
        expect(self.empty_heart_icon).to_be_visible()
        self.delete_btn.click()
        expect(self.delete_popup).to_be_visible()
        self.delete_from_cart_popup_btn.click()
        return self

    def buy_book(self):
        expect(self.checkout_total).not_to_be_empty()
        self.checkout_btn.click()



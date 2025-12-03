import re

import allure
from playwright.sync_api import Page, expect
from utils import close_promo_popup, allure_screenshot
from data.books import Book



class CartPage:
    def __init__(self, page: Page, book: Book):
        self.page = page
        self.book = book
        self.add_to_cart_btn = page.get_by_test_id("book__addToCartButton")
        self.already_in_the_cart_btn = page.get_by_test_id("book__goToCartButton")
        self.delete_btn = page.get_by_test_id("cart__listDeleteButton")
        self.delete_popup = page.get_by_test_id("cart__modalDeleteArt")
        self.delete_and_postpone_btn = page.get_by_role("button", name="Отложить и удалить")
        self.empty_heart_icon = page.get_by_role("button", name="Отложить").get_by_test_id("icon_favorites")
        self.filled_heart_icon = page.get_by_role("button", name="В отложенном").get_by_test_id("icon_favoritesFilled")
        self.delete_from_cart_popup_btn = page.get_by_test_id("cart__modalDeleteArt--button-primary")
        self.checkout_btn = page.get_by_role("button", name="Перейти к покупке")
        self.checkout_total = page.get_by_test_id("cart__checkout--total")
        self.empty_cart_state = page.get_by_test_id("cart__emptyState--wrapper")


    def get_book_locator(self):
        if not self.book.id:
            raise ValueError("Book ID is required to locate item in cart")
        return self.page.get_by_test_id(f"cart__listItem--{self.book.id}")

    @allure.step("Открывается страница книги, книга добавляется в корзину. Осуществляется переход на станицу корзины")
    def navigate_and_add_to_cart(self):
        self.page.goto(self.book.url, wait_until='domcontentloaded')
        book_title = self.page.get_by_role("heading", name=self.book.title)
        book_title.wait_for(state="visible")
        self.add_to_cart_btn.click()
        self.page.wait_for_timeout(1000)
        close_promo_popup(self.page)
        self.already_in_the_cart_btn.click()
        allure_screenshot(self.page)


    @allure.step("Добавление книги в отложенное")
    def postpone_book(self):
        book_in_cart = self.get_book_locator()
        book_in_cart.get_by_role("button", name="Отложить").click()
        allure_screenshot(self.page)
        return self

    @allure.step("Книга не в отложенном. Удаление книги -> в поп апе нажимается 'Удалить и отложить'")
    def delete_from_cart_and_postpone (self):
        expect(self.empty_heart_icon).to_be_visible()
        allure_screenshot(self.page)
        self.page.wait_for_timeout(1000)
        self.delete_btn.click()
        expect(self.delete_popup).to_be_visible()
        allure_screenshot(self.page)
        self.delete_and_postpone_btn.click()
        return self

    @allure.step("Книга не в отложенном. Удаление книги без добавления в отложенное")
    def delete_from_cart (self):
        expect(self.empty_heart_icon).to_be_visible()
        allure_screenshot(self.page)
        self.page.wait_for_timeout(1000)
        self.delete_btn.click()
        expect(self.delete_popup).to_be_visible()
        allure_screenshot(self.page)
        self.delete_from_cart_popup_btn.click()
        return self

    @allure.step("Нажать на  кнопку 'Перейти к покупке'")
    def buy_book(self):
        self.page.wait_for_timeout(3000)
        expect(self.checkout_total).to_have_text(re.compile(r".+"))
        self.checkout_btn.click()

    @allure.step("Книга в отложенном. Удаление книги без добавления в отложенное")
    def delete_from_cart_already_postponed_book(self):
        book_in_cart = self.get_book_locator()
        book_in_cart.get_by_role("button", name="Отложить").click()
        allure_screenshot(self.page)
        self.page.wait_for_timeout(1000)
        self.delete_btn.click(timeout=1000)
        expect(self.delete_popup).to_be_visible()
        allure_screenshot(self.page)
        self.delete_from_cart_popup_btn.click()
        return self

    @allure.step("Проверка того, что после удаления книги корзина становится пуста")
    def cart_is_empty(self):
        expect(self.empty_cart_state).to_have_text(re.compile(r"Корзина пуста"))
        allure_screenshot(self.page)
        return self
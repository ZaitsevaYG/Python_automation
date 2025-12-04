import allure
from playwright.sync_api import Page, expect
import re
from playwright.sync_api import Error
from utils import close_promo_popup, allure_screenshot
from data.books import Book


class BookPage:
    def __init__(self, page: Page, book: Book):
        self.page = page
        self.book = book
        self.text_book_btn = page.get_by_role("link", name="Текст")
        self.audio_book_btn = page.get_by_test_id("book-tabs-format__wrapper").get_by_role("link", name="Аудио")
        self.favorite_btn = page.get_by_test_id("book-sale-block__wrapper").get_by_role("button", name="Отложить")
        self.with_subscription_btn = page.get_by_role("button", name="Читать по подписке")
        self.buy_download_btn = page.get_by_role("button", name="Купить и скачать")
        self.add_to_cart_btn = page.get_by_test_id("book__addToCartButton")
        self.read_the_fragment_btn = page.get_by_test_id("book__fragmentReadListen--button")
        self.listen_to_the_fragment_btn =  page.get_by_test_id("book-tabs-format__wrapper").get_by_role("link", name="Аудио")
        self.already_in_the_cart_btn = page.get_by_test_id("book__goToCartButton")
        self.paper_book_banner = page.get_by_text("Теперь и бумажные книги")
        self.buy_paper_book_btn = page.get_by_role("button", name=re.compile(r"Купить за"))
        self.details_paper_book_btn = page.get_by_role("button", name="Подробнее")
        self.buy_from_details_paper_book_btn = page.get_by_test_id("button__content").get_by_role("button", name="Купить")
        self.already_in_the_cart_btn = page.get_by_test_id("book__goToCartButton")

    @allure.step("Открывается страница книги. Пользователь не авторизован")
    def navigate(self):
        self.page.goto(self.book.url, wait_until='domcontentloaded', timeout=60000)
        expect(self.page.get_by_test_id("tab-login").get_by_role("paragraph")).to_contain_text("Войти")
        book_title = self.page.get_by_role("heading", name=self.book.title)
        book_title.wait_for(state="visible")
        allure_screenshot(self.page)

    @allure.step("Нажать на кнопку текстовой версии книги")
    def choose_text_version(self):
        self.text_book_btn.click()
        return self

    @allure.step("Нажать на кнопку аудио версии книги")
    def choose_audio_version(self):
        self.audio_book_btn.click(timeout=1000)
        return self

    @allure.step("Добавить книгу в избранное")
    def make_favorite(self):
        self.favorite_btn.click(timeout=1000)
        return self

    @allure.step("Нажать на кнопку 'Взять по подписке'")
    def read_with_subscription(self):
        self.with_subscription_btn.is_visible()
        self.with_subscription_btn.click(timeout=1000)
        return self

    @allure.step("Нажать на кнопку 'Купить и скачать'")
    def buy_and_download(self):
        self.buy_download_btn.click(timeout=1000)
        return self

    @allure.step("Нажать на кнопку 'Добавить в корзину'")
    def add_to_cart(self):
        self.add_to_cart_btn.click()
        close_promo_popup(self.page)

    @allure.step("Проверка, добавилась ли книга в избранное - поменялась ли икона на странице книги")
    def is_in_favorites(self) -> bool:
        filled_icon = self.page.get_by_role("button", name="Отложить").get_by_test_id("icon_favoritesFilled")
        allure_screenshot(self.page)
        return filled_icon.is_visible(timeout=5000)


    @allure.step("Проверка, добавилась ли книга в корзину - поменялся ли индекс на иконке корзины")
    def is_in_cart(self) -> bool:
        cart_counter = self.page.get_by_test_id("header__cart--counter")
        allure_screenshot(self.page)
        try:
            cart_counter.wait_for(state="visible", timeout=5000)
            text = cart_counter.text_content().strip()
            if not text:

                return False
            numbers = re.findall(r'\d+', text)
            result = bool(numbers and int(numbers[0]) > 0)


            if result:
                allure_screenshot(self.page)

            return result
        except Error:

            allure_screenshot(self.page)
            return False


    @allure.step("Добавление книги в избранное, если она еще не там")
    def ensure_in_favorites(self):
        if not self.is_in_favorites():
            self.make_favorite()



import allure
from playwright.sync_api import Page, expect

from data.books import main_link
from utils.utils import allure_screenshot


class StartPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_field = page.locator('input[data-testid="search__input"]')
        self.search_btn = page.locator('button[data-testid="search__button"]')
        self.search_result_title = page.locator('a[data-testid="art__title"]')
        self.search_result_author = page.locator('a[data-testid="art__authorName--link"]')
        self.search_result_nothing_found = page.get_by_test_id('search-title__wrapper')

    @allure.step("Открывается стартовая страница. Пользователь не авторизован")
    def navigate(self):
        self.page.goto(main_link, wait_until='domcontentloaded', timeout=60000)
        expect(self.page.get_by_test_id("tab-login").get_by_role("paragraph")).to_contain_text("Войти")
        self.page.wait_for_selector('input[data-testid="search__input"]', state='visible')

    @allure.step("Вводится имя автора в строку поиска и нажать кнопку поиска")
    def search_by_author(self, book):
        self.search_field.fill(book.author)
        self.search_btn.click()

        return self

    @allure.step("Вводится название книги в строку поиска и нажать кнопку поиска")
    def search_by_title(self, book):
        self.search_field.fill(book.title)
        self.search_btn.click()
        return self

    @allure.step("Проверка, что первая найденная книга соответствует критериям поиска")
    def book_with_specified_title_must_be_found (self, book):
        try:
            self.page.wait_for_selector('a[data-testid="art__title"]', state='visible')
            first_title =self.search_result_title.first

            expect(first_title).to_contain_text(book.title)

        except Exception as e:
            allure_screenshot(self.page)
            raise e
        return self

    @allure.step("Проверка, что первая найденная книга соответствует критериям поиска")
    def book_with_specified_author_must_be_found (self, book):
        try:
            self.page.wait_for_selector('a[data-testid="art__authorName--link"]', state='visible')
            first_author = self.search_result_author.first
            expect(first_author).to_contain_text(book.author)

        except Exception as e:
            allure_screenshot(self.page)
            raise e
        return self

    @allure.step("Проверка того, что по несуществующему названию появляется текст об отсутствии результатов поиска")
    def nothing_found_bad_request(self):
        try:
            allure_screenshot(self.page)
            expect(self.search_result_nothing_found).to_contain_text("ничего не найдено")
        except Exception as e:
            allure_screenshot(self.page)
            raise e

        return self


def start_page():
    return None
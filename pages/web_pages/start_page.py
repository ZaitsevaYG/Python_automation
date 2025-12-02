from playwright.sync_api import Page, expect
from allure import step


class StartPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_field = page.locator('input[data-testid="search__input"]')
        self.search_btn = page.locator('button[data-testid="search__button"]')
        self.search_result_title = page.locator('a[data-testid="art__title"]')
        self.search_result_author = page.locator('a[data-testid="art__authorName--link"]')
        self.search_result_nothing_found = page.get_by_test_id('search-title__wrapper')

    @step("Открывается стартовая страница")
    def navigate(self):
        self.page.goto('https://www.litres.ru/', wait_until='domcontentloaded', timeout=60000)
        self.page.wait_for_selector('input[data-testid="search__input"]', state='visible')

    @step("Поиск по автору")
    def search_by_author(self, book):
        self.search_field.fill(book.author)
        self.search_btn.click()
        return self

    @step("Поиск по названию книги")
    def search_by_title(self, book):
        self.search_field.fill(book.title)
        self.search_btn.click()
        return self

    @step("Проверка того, что по названию найдена верная книга")
    def book_with_specified_title_must_be_found (self, book):
        self.page.wait_for_selector('a[data-testid="art__authorName--link"]', state='visible')
        first_title =self.search_result_title.first
        expect(first_title).to_contain_text(book.title)
        return self

    @step("Проверка того, что по автору найдена верная книга")
    def book_with_specified_author_must_be_found (self, book):
        first_author = self.search_result_author.first
        expect(first_author).to_contain_text(book.author)
        return self

    @step("Проверка того, что по несуществующему названию появляется текст об отсутствии результатов поиска")
    def nothing_found_bad_request(self):
        expect(self.search_result_nothing_found).to_contain_text("ничего не найдено")
        return self


def start_page():
    return None
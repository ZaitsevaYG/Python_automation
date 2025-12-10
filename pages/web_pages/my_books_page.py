import allure
from playwright.sync_api import Page, expect
from utils.utils import allure_screenshot
from data.books import Book, main_link


class MyBooksPage:
    def __init__(self, page: Page, book: Book):
        self.page = page
        self.book = book
        self.my_books = page.get_by_test_id("tab-myBooks").get_by_test_id("tab__link")
        self.authorization_from_my_books = page.get_by_test_id("myBooks__login--button")
        self.my = page.get_by_role("tab", name="Мои").locator('a[data-testid="navigation__tabItem__link"]')
        self.postponed = page.get_by_role("tab", name="Отложено").locator('a[data-testid="navigation__tabItem__link"]')
        self.cloud = page.get_by_role("tab", name="Облако").locator('a[data-testid="navigation__tabItem__link"]')
        self.lists = page.get_by_role("tab", name="Списки").locator('a[data-testid="navigation__tabItem__link"]')
        self.i_follow = page.get_by_role("tab", name="Я слежу").locator('a[data-testid="navigation__tabItem__link"]')
        self.my_wrapper = page.locator('[data-testid="navigation__tabItem--wrapper"]').filter(has_text="Мои")
        self.postponed_wrapper = page.locator('[data-testid="navigation__tabItem--wrapper"]').filter(has_text="Отложено")
        self.cloud_wrapper = page.locator('[data-testid="navigation__tabItem--wrapper"]').filter(has_text="Облако")
        self.lists_wrapper = page.locator('[data-testid="navigation__tabItem--wrapper"]').filter(has_text="Списки")
        self.i_follow_wrapper = page.locator('[data-testid="navigation__tabItem--wrapper"]').filter(has_text="Я слежу")
        self.find_to_follow = page.get_by_role("button", name="Найти на кого подписаться")
        self.fill_list = page.get_by_role("button", name="Наполнить список")
        self.my_choose_books = page.get_by_role("button", name="Выбрать книги")
        self.my_empty_inner_text = page.get_by_text("Здесь будут книги, которые вы купите или возьмете по Абонементу или по акции")
        self.postponed_empty_inner_text = page.get_by_text("Здесь будет все, что вы отложите на потом")
        self.cloud_upload_from_pc = page.get_by_role("heading", name="Загрузить книгу с моего компьютера")
        self.cloud_upload_file_btn = page.get_by_role("button", name="Выбрать файл")
        self.cloud_learn_more = page.get_by_role("button", name="Узнать больше")
        self.archive = page.get_by_role("tab", name="Архив").locator('a[data-testid="navigation__tabItem__link"]')
        self.archive_wrapper = page.locator('[data-testid="navigation__tabItem--wrapper"]').filter(has_text="Архив")
        self.archive_empty_inner_text = page.get_by_text("В Архиве нет книг.Вы всегда сможете легко восстановить из Архива любую книгу")
        self.lists_empty_inner_text = page.get_by_text("Создавайте списки для удобства и делитесь ими с другими")
        self.i_follow_search = page.get_by_role("button", name="Найти на кого подписаться")
        self.i_follow_fill_the_lists = page.get_by_role("button", name="Наполнить список")
        self.upload_books_btn = page.get_by_role("button", name="Загрузить книги")
        self.recommended = page.get_by_test_id("breadcrumbs__wrapper").get_by_text("Рекомендации для вас")
        self.recommended_url = f'{main_link}recommend/'
        self.login = page.get_by_test_id("tab-login").get_by_role("paragraph")
        self.recommended_for_u_title = page.get_by_test_id("pageTitle").get_by_text("Рекомендации для вас")


    @allure.step("Открывается страница 'Мои книги'. Пользователь не авторизован")
    def navigate(self):
        self.page.goto(f"{main_link}my-books/purchased/", wait_until='domcontentloaded', timeout=60000)
        expect(self.login).to_contain_text("Войти")


    @allure.step("Проверка возможности авторизоваться из окна 'Мои книги'")
    def my_books_auth(self):
        expect(self.page.get_by_test_id("myBooks__readAndListen--section").get_by_text("Здесь будет появляться все, что вы читаете и слушаете")).to_be_visible()
        self.authorization_from_my_books.click()
        self.page.wait_for_timeout(5000)
        allure_screenshot(self.page)


    @allure.step("Проверка отображения вкладки 'Мои'")
    def my_books_tab(self):
        self.my.click()
        self.page.wait_for_timeout(1000)
        expect(self.my_wrapper).to_have_attribute("aria-selected","true")
        allure_screenshot(self.page)
        expect(self.my_empty_inner_text).to_be_visible()

    @allure.step("Проверка отображения вкладки 'Отложено'")
    def postponed_books_tab(self):
        self.postponed.click()
        self.page.wait_for_timeout(1000)
        expect(self.postponed_wrapper).to_have_attribute("aria-selected","true")
        allure_screenshot(self.page)
        expect(self.postponed_empty_inner_text).to_be_visible()

    @allure.step("Проверка отображения вкладки 'Облако'")
    def cloud_tab(self):
        self.cloud.click()
        self.page.wait_for_timeout(1000)
        expect(self.cloud_wrapper).to_have_attribute("aria-selected", "true")
        allure_screenshot(self.page)
        expect(self.cloud_upload_from_pc).to_be_visible()


    @allure.step("Проверка отображения вкладки 'Облако' - 'Узнать больше'")
    def cloud_learn_more(self):
        self.cloud.click()
        self.page.wait_for_timeout(1000)
        expect(self.cloud_wrapper).to_have_attribute("aria-selected", "true")
        self.cloud_learn_more.click()
        self.page.wait_for_timeout(1000)
        allure_screenshot(self.page)
        expect(self.page.get_by_test_id("modal--content")).to_contain_text("Загрузка книг в облако")
        self.page.get_by_test_id("modal--close-button").click()

    @allure.step("Проверка отображения вкладки 'Списки'")
    def lists_tab(self):
        self.lists.click()
        self.page.wait_for_timeout(1000)
        expect(self.lists_wrapper).to_have_attribute("aria-selected", "true")
        allure_screenshot(self.page)
        expect(self.lists_empty_inner_text).to_be_visible()

    @allure.step("Проверка отображения вкладки 'Я слежу'")
    def i_follow_tab(self):
        self.i_follow.click()
        self.page.wait_for_timeout(1000)
        expect(self.i_follow_wrapper).to_have_attribute("aria-selected", "true")
        allure_screenshot(self.page)
        expect(self.i_follow_search).to_be_visible()
        expect(self.i_follow_fill_the_lists).to_be_visible()

    @allure.step("Проверка отображения вкладки 'Архив'")
    def archive_tab(self):
        self.archive.click()
        self.page.wait_for_timeout(1000)
        expect(self.archive_wrapper).to_have_attribute("aria-selected", "true")
        allure_screenshot(self.page)
        expect(self.archive_empty_inner_text).to_be_visible()

    @allure.step("Проверка кнопки 'Загрузить книги'")
    def upload_books(self):
        self.upload_books_btn.click()
        self.page.wait_for_timeout(1000)
        allure_screenshot(self.page)
        expect(self.cloud_wrapper).to_have_attribute("aria-selected", "true")
        expect(self.cloud_upload_from_pc).to_be_visible()

    @allure.step("Проверка возможности добавить книгу в отложенное без авторизации. Проверка элементов на странице.")
    def one_postponed_book(self, book):
        self.postponed.click()
        self.page.wait_for_timeout(1000)
        expect(self.postponed_wrapper).to_have_attribute("aria-selected", "true")
        allure_screenshot(self.page)
        expect(self.page.get_by_test_id("navigation__tabItem__counter")).to_contain_text("1")
        expect(self.page.get_by_test_id("art__title")).to_contain_text(book.title)







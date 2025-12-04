from playwright.sync_api import expect

from data.books import main_link
from utils import close_authorization_popup, allure_screenshot
import allure

@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности авторизоваться на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_mybooks_authorization(mybooks_page):
    mybooks_page.my_books_auth()
    close_authorization_popup(mybooks_page)

@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка элементов на вкладке Мои на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_my_books_tab(mybooks_page):
    expected_url = f'{main_link}purchased/'
    mybooks_page.my_books_tab()
    mybooks_page.my_choose_books.click()
    mybooks_page.page.wait_for_url(expected_url)
    mybooks_page.page.wait_for_timeout(3000)
    expect(mybooks_page.recommended).to_be_visible()

@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка элементов на вкладке Отложено на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_postponed_books_tab(mybooks_page):
    expected_url = f'{main_link}purchased/'
    mybooks_page.postponed_books_tab()
    mybooks_page.my_choose_books.click()
    mybooks_page.page.wait_for_url(expected_url)
    mybooks_page.page.wait_for_timeout(3000)
    expect(mybooks_page.recommended).to_be_visible()

@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка элементов на вкладке Облако на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_cloud_tab(mybooks_page):
    mybooks_page.my_cloud_tab()
    mybooks_page.cloud_upload_file_btn.click()
    mybooks_page.page.wait_for_timeout(3000)
    allure_screenshot(mybooks_page)
    close_authorization_popup(mybooks_page)


@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка элементов на вкладке Списки на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_lists_tab(mybooks_page):
    mybooks_page.my_lists_tab()
    
from playwright.sync_api import expect

from data.books import FLOWERS
from pages.web_pages.book_page import BookPage
from pages.web_pages.my_books_page import MyBooksPage
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
    close_authorization_popup(mybooks_page.page)

@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка элементов на вкладке Мои на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_my_books_tab(mybooks_page):

    mybooks_page.my_books_tab()
    mybooks_page.my_choose_books.click()
    #mybooks_page.page.wait_for_url(mybooks_page.recommended_url)
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

    mybooks_page.postponed_books_tab()
    mybooks_page.my_choose_books.click()
    #mybooks_page.page.wait_for_url(mybooks_page.recommended_url)
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
    mybooks_page.cloud_tab()
    mybooks_page.cloud_upload_file_btn.click()
    mybooks_page.page.wait_for_timeout(3000)
    allure_screenshot(mybooks_page.page)
    close_authorization_popup(mybooks_page.page)


@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка элементов на вкладке Списки на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_lists_tab(mybooks_page):
    mybooks_page.lists_tab()


@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка элементов на вкладке Я слежу - Найти на кого подписаться на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_i_follow_tab_my_person(mybooks_page):
    mybooks_page.i_follow_tab()
    mybooks_page.page.wait_for_timeout(3000)
    allure_screenshot(mybooks_page.page)
    mybooks_page.i_follow_search.click()
    mybooks_page.page.wait_for_timeout(3000)
    #mybooks_page.page.wait_for_url(mybooks_page.recommended_url)
    expect(mybooks_page.recommended).to_be_visible()

@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка элементов на вкладке Я слежу - Наполнить список  на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_i_follow_tab_fill_the_list(mybooks_page):
    mybooks_page.i_follow_tab()
    mybooks_page.page.wait_for_timeout(3000)
    allure_screenshot(mybooks_page.page)
    mybooks_page.i_follow_fill_the_lists.click()
    mybooks_page.page.wait_for_timeout(3000)
    #mybooks_page.page.wait_for_url(mybooks_page.recommended_url)
    expect(mybooks_page.recommended).to_be_visible()

@allure.epic('Проверка элементов на странице Мои книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка элементов на вкладке Архив на странице Мои книги")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_archive_button(mybooks_page):
    mybooks_page.archive.click()
    mybooks_page.page.wait_for_timeout(3000)
    allure_screenshot(mybooks_page.page)
    expect(mybooks_page.archive_empty_inner_text).to_be_visible()



def test_postponed_without_auth_page_my_books(page):
    book_page = BookPage(page,FLOWERS)
    book_page.navigate()
    book_page.make_favorite()
    mybooks_page = MyBooksPage(page,FLOWERS)
    mybooks_page.navigate()



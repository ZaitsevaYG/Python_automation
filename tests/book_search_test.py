from data.books import Book
from pages.start_page import StartPage


def test_searching_by_title (page):
    start_page = StartPage(page)
    book = Book(
        title='Маленькие женщины',
        author='',
        url='',
        price=''
    )

    start_page.navigate()
    start_page.search_by_title(book)
    start_page.book_with_specified_title_must_be_found(book)

def test_searching_by_author (page):
    start_page = StartPage(page)
    book = Book(
        title='',
        author='Стивен Кинг',
        url='',
        price=''
    )

    start_page.navigate()
    start_page.search_by_author(book)
    start_page.book_with_specified_author_must_be_found(book)


def test_non_existing_search(page):
    start_page = StartPage(page)
    book = Book(
        title='jewgfjsnfhjh',
        author='',
        url='',
        price=''
    )

    start_page.navigate()
    start_page.search_by_title(book)
    start_page.nothing_found_change_request()
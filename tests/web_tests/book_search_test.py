from data.books import Book
import allure

@allure.epic('Поиск книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности найти книгу по разным параметрам")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_searching_by_title (start_page):

    book = Book(
        title='Маленькие женщины',
        author='',
        url='',
        price=''
    )

    start_page.search_by_title(book)
    start_page.book_with_specified_title_must_be_found(book)


@allure.epic('Поиск книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности найти книгу по разным параметрам")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_searching_by_author (start_page):

    book = Book(
        title='',
        author='Стивен Кинг',
        url='',
        price=''
    )

    start_page.search_by_author(book)
    start_page.book_with_specified_author_must_be_found(book)

@allure.epic('Поиск книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности найти книгу по разным параметрам")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_non_existing_search(start_page):

    book = Book(
        title='jewgfjsnfhjh',
        author='',
        url='',
        price=''
    )

    start_page.search_by_title(book)
    start_page.nothing_found_bad_request()
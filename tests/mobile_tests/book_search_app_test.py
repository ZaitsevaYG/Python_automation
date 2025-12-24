import allure

from data.books import NIGHT_CLERK
from pages.mobile_pages_android.book_search_page_app import book_search_page


@allure.epic('Поиск')
@allure.label("owner", "Zaitseva Yana")
@allure.feature("Проверка функции поиска книги в мобильном приложении - существующая книга")
@allure.severity('normal')
@allure.label('layer', 'mobile')

def test_successful_searching_book(android_mobile_management):

        book_search_page.searching_book(NIGHT_CLERK)
        book_search_page.book_must_be_found(NIGHT_CLERK)


@allure.epic('Поиск')
@allure.label("owner", "Zaitseva Yana")
@allure.feature("Проверка функции поиска книги в мобильном приложении - несуществующая книга")
@allure.severity('normal')
@allure.label('layer', 'mobile')

def test_unsuccessful_searching_book(android_mobile_management):

        book_search_page.searching_non_existent_book()
        book_search_page.book_must_not_be_found()
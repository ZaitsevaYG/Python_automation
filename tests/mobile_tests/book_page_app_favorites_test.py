import allure

from data.books import NIGHT_CLERK
from pages.mobile_pages_android.book_search_page_app import book_search_page
from pages.mobile_pages_android.book_page_app import book_page


@allure.epic('Избранное')
@allure.label("owner", "Zaitseva Yana")
@allure.feature("Добавление книги в избранное")
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_add_to_favorites(android_mobile_management):
    book_search_page.searching_book(NIGHT_CLERK)
    book_search_page.choosing_book()
    book_page.adding_book_to_saved()
    book_page.go_to_saved_tab()
    book_page.book_must_be_added_to_saved(NIGHT_CLERK)


@allure.epic('Избранное')
@allure.label("owner", "Zaitseva Yana")
@allure.feature("Удаление книги из избранного")
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_remove_from_favorites(android_mobile_management):
    book_search_page.searching_book(NIGHT_CLERK)
    book_search_page.choosing_book()
    book_page.adding_book_to_saved()
    book_page.removing_book_from_saved()
    book_page.go_to_saved_tab()
    book_page.book_must_be_removed_from_saved()
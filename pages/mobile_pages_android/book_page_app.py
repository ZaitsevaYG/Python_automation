import allure
from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy
from data.books import Book


class AndroidBookPage:
    book = Book()

    @allure.step('Добавление книги в избранное')
    def adding_book_to_saved(self):
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/imageViewBookCardFavourite")).click()
        return self

    @allure.step('Переход на страницу "Отложенное"')
    def go_to_saved_tab(self):
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/nav_my_audiobooks")).click()
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/textViewBookSectionTitle")).with_(timeout=30).click()
        return self

    @allure.step('Проверка, что книга добавлена в избранное')
    def book_must_be_added_to_saved(self, book):
        (browser.element((AppiumBy.ID, "ru.litres.android.international:id/textViewBookName"))
         .should(have.text(book.title)))
        return self

    @allure.step('Удаление книги из избранного')
    def removing_book_from_saved(self):
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/textViewBookName")).click()
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/imageViewBookCardFavourite")).with_(timeout=30).click()
        return self

    @allure.step('Проверка, что книга удалена из избранного')
    def book_must_be_removed_from_saved(self):
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/nav_my_audiobooks")).with_(timeout=30).click()
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/textViewBookSectionTitle")).click()
        (browser.element((AppiumBy.ID, "ru.litres.android.international:id/textViewDescriptionEmptySection"))
         .should(have.text("Здесь будет все, что вы отложите\nна потом")))
        return self

book_page = AndroidBookPage()
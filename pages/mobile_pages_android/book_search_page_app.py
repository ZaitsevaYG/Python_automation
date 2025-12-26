from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy

from data.books import Book


class AndroidSearchBookPage:
    book = Book()

    def searching_book(self, book):
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/search")).click()
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/et_search_query")).type(book.title)
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/textViewItemSearchSuggestText")).with_(timeout=30).click()
        return self

    def book_must_be_found(self, book):

        (browser.element((AppiumBy.ID, "ru.litres.android.international:id/textViewBookName"))
        .should(have.text(book.title)))
        return self

    def searching_non_existent_book(self):
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/search")).click()
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/et_search_query")).type('fhdrtrshrsf')
        browser.element((AppiumBy.ID, "ru.litres.android.international:id/textViewItemSearchSuggestText")).click()
        return self

    def book_must_not_be_found(self):

        browser.element((AppiumBy.ID, "ru.litres.android.international:id/title")).should(have.text('Ничего не найдено'))
        (browser.element((AppiumBy.ID, "ru.litres.android.international:id/tv_books_search_empty_message"))
        .should(have.text('Убедитесь, что вы правильно написали поисковый запрос')))
        return self

    def choosing_book(self):
        browser.element((AppiumBy.XPATH, "(//android.widget.TextView[@resource-id='ru.litres.android.international:id/textViewBookName'])[1]")).click()
        return self


book_search_page = AndroidSearchBookPage()
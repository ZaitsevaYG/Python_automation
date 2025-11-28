from playwright.async_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_btn = page.get_by_test_id("book__addToCartButton")
        self.close_popup_btn = page.get_by_test_id("modal__close--button")
        self.already_in_the_cart_btn = page.get_by_test_id("book__goToCartButton")
        self.set_the_book_aside_btn = page.get_by_test_id("cart__listItem--50390816").get_by_role("button", name="Отложить")


    def navigate_and_add_to_cart(self):
        self.page.goto('https://www.litres.ru/book/dzheyms-klir/atomnye-privychki-kak-priobresti-horoshie-privychki-i-izbavit-48514275/', wait_until='domcontentloaded')
        book_title = self.page.get_by_role("heading", name="Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих")
        book_title.wait_for(state="visible")
        self.add_to_cart_btn.click()

        if self.close_popup_btn.is_visible(timeout=3000):
            self.close_popup_btn.click()
            self.close_popup_btn.wait_for(state="hidden", timeout=5000)

        self.already_in_the_cart_btn.is_visible(timeout=1000)
        self.already_in_the_cart_btn.click()
        self.page.wait_for_timeout(timeout=1000)

    def postpone_book(self):
        self.set_the_book_aside_btn.click()
        return self

    def is_in_postponed(self) -> bool:
        filled_icon = self.page.get_by_role("button", name="В отложенном").get_by_test_id("icon_favoritesFilled")
        return filled_icon.is_visible(timeout=5000)






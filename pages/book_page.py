from playwright.sync_api import Page, expect
import re
from playwright.sync_api import Error

class BookPage:
    def __init__(self, page: Page):
        self.page = page
        self.text_book_btn = page.get_by_role("link", name="Текст")
        self.audio_book_btn = page.get_by_test_id("book-tabs-format__wrapper").get_by_role("link", name="Аудио")
        self.favorite_btn = page.get_by_test_id("book-sale-block__wrapper").get_by_role("button", name="Отложить")
        self.with_subscription_btn = page.get_by_role("button", name="Читать по подписке")
        self.buy_download_btn = page.get_by_role("button", name="Купить и скачать")
        self.add_to_cart_btn = page.get_by_test_id("book__addToCartButton")
        self.read_the_fragment_btn = page.get_by_test_id("book__fragmentReadListen--button")
        self.listen_to_the_fragment_btn =  page.get_by_test_id("book-tabs-format__wrapper").get_by_role("link", name="Аудио")
        self.close_auth_popup_btn = page.get_by_test_id("authorization-popup__close-button")
        self.close_popup_btn = page.get_by_test_id("modal__close--button")
        self.already_in_the_cart_btn = page.get_by_test_id("book__goToCartButton")
        self.authorization_popup = page.get_by_test_id("authorization-popup")
        self.paper_book_banner = page.get_by_text("Теперь и бумажные книги")
        self.buy_paper_book_btn = page.get_by_role("button", name=re.compile(r"Купить за"))
        self.details_paper_book_btn = page.get_by_role("button", name="Подробнее")
        self.buy_from_details_paper_book_btn = page.get_by_test_id("modalWindow--content").get_by_role("button", name="Купить")
        self.paper_book_title_details_popup = page.get_by_test_id("modalWindow--content").get_by_role("heading", name="Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих")

    def navigate(self):
        self.page.goto('https://www.litres.ru/book/dzheyms-klir/atomnye-privychki-kak-priobresti-horoshie-privychki-i-izbavit-48514275/', wait_until='domcontentloaded')
        book_title = self.page.get_by_role("heading", name="Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих")
        book_title.wait_for(state="visible")


    def choose_text_version(self):
        self.text_book_btn.click()
        return self

    def choose_audio_version(self):
        self.audio_book_btn.click()
        return self

    def make_favorite(self):
        self.favorite_btn.click()
        return self

    def read_with_subscription(self):
        self.with_subscription_btn.is_visible()
        self.with_subscription_btn.click()
        return self

    def buy_and_download(self):
        self.buy_download_btn.click()
        return self

    def add_to_cart(self):
        self.add_to_cart_btn.click()


        if self.close_popup_btn.is_visible(timeout=3000):
            self.close_popup_btn.click()
            self.close_popup_btn.wait_for(state="hidden", timeout=5000)
        return self

    def is_in_favorites(self) -> bool:
        filled_icon = self.page.get_by_role("button", name="Отложить").get_by_test_id("icon_favoritesFilled")
        return filled_icon.is_visible(timeout=5000)


    def is_in_cart(self) -> bool:
        cart_counter = self.page.get_by_test_id("header__cart--counter")
        try:
            cart_counter.wait_for(state="visible", timeout=5000)
            text = cart_counter.text_content().strip()
            if not text:
                return False
            numbers = re.findall(r'\d+', text)
            return bool(numbers and int(numbers[0]) > 0)
        except Error:

            return False


    def ensure_in_favorites(self):
        if not self.is_in_favorites():
            self.make_favorite()







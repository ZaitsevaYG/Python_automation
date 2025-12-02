
from playwright.sync_api import expect
from utils import close_authorization_popup

def test_choosing_text_version(book_page):
    book_page.choose_text_version()
    expect(book_page.read_the_fragment_btn).to_be_visible()

def test_choosing_audio_version(book_page):
    book_page.choose_audio_version()
    expect(book_page.listen_to_the_fragment_btn).to_be_visible()

def test_add_to_favorites (book_page):
    assert not book_page.is_in_favorites()
    book_page.make_favorite()
    assert book_page.is_in_favorites()

def test_remove_from_favorites (book_page):
    book_page.ensure_in_favorites()
    assert book_page.is_in_favorites()
    book_page.make_favorite()
    assert not book_page.is_in_favorites()

def test_add_to_cart (book_page):

    book_page.add_to_cart()
    book_page.page.wait_for_timeout(1000)
    assert book_page.is_in_cart()
    expect(book_page.already_in_the_cart_btn).to_be_visible()
    expect(book_page.already_in_the_cart_btn).to_have_text("В корзинеПерейти")

def test_buy_and_download(book_page):
    book_page.buy_and_download()
    book_page.page.wait_for_timeout(1000)
    close_authorization_popup(book_page.page)
    assert not book_page.is_in_cart()

def test_read_with_subscription(book_page):
    book_page.read_with_subscription()
    book_page.page.wait_for_timeout(1000)
    close_authorization_popup(book_page.page)
    assert not book_page.is_in_cart()

def test_buy_paper_book(book_page):
    book_page.buy_paper_book_btn.click()
    book_page.page.wait_for_timeout(1000)
    close_authorization_popup(book_page.page)
    assert not book_page.is_in_cart()

# def test_details_paper_book(book_page):
#     book_page.details_paper_book_btn.click()
#     book_page.page.wait_for_timeout(1000)
#     book_page.paper_book_popup_title()
#     expect(book_page.buy_from_details_paper_book_btn).to_be_visible()
#     book_page.buy_from_details_paper_book_btn.click()
#     book_page.page.wait_for_timeout(1000)
#     close_authorization_popup(book_page.page)
#     assert not book_page.is_in_cart()
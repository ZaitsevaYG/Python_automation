from playwright.sync_api import expect
from utils.utils import close_authorization_popup, close_promo_popup, allure_screenshot
import allure

@allure.epic('Проверка элементов на странице книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности выбрать аудио и текстовую версию")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_choosing_text_version(book_page):
    book_page.choose_text_version()
    expect(book_page.read_the_fragment_btn).to_be_visible()
    allure_screenshot(book_page.page)


@allure.epic('Проверка элементов на странице книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности выбрать аудио и текстовую версию")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_choosing_audio_version(book_page):
    book_page.choose_audio_version()
    expect(book_page.listen_to_the_fragment_btn).to_be_visible()
    allure_screenshot(book_page.page)

@allure.epic('Проверка элементов на странице книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности добавить/удалить из избранного")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_to_favorites (book_page):
    assert not book_page.is_in_favorites()
    allure_screenshot(book_page.page)
    book_page.make_favorite()
    assert book_page.is_in_favorites()
    allure_screenshot(book_page.page)

@allure.epic('Проверка элементов на странице книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности добавить/удалить из избранного")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_remove_from_favorites (book_page):
    book_page.ensure_in_favorites()
    allure_screenshot(book_page.page)
    assert book_page.is_in_favorites()
    book_page.make_favorite()
    assert not book_page.is_in_favorites()
    allure_screenshot(book_page.page)

@allure.epic('Проверка элементов на странице книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности приобрести книгу")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critic')
@allure.label('layer', 'web')
def test_add_to_cart (book_page):
    book_page.add_to_cart()
    book_page.page.wait_for_timeout(1000)
    close_promo_popup(book_page.page)
    assert book_page.is_in_cart()
    expect(book_page.already_in_the_cart_btn).to_be_visible()
    expect(book_page.already_in_the_cart_btn).to_have_text("В корзинеПерейти")


@allure.epic('Проверка элементов на странице книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности приобрести книгу")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critic')
@allure.label('layer', 'web')
def test_buy_and_download(book_page):
    book_page.buy_and_download()
    book_page.page.wait_for_timeout(1000)
    close_authorization_popup(book_page.page)
    assert not book_page.is_in_cart()

@allure.epic('Проверка элементов на странице книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности приобрести книгу")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critic')
@allure.label('layer', 'web')
def test_read_with_subscription(book_page):
    book_page.read_with_subscription()
    book_page.page.wait_for_timeout(1000)
    close_authorization_popup(book_page.page)
    assert not book_page.is_in_cart()

@allure.epic('Проверка элементов на странице книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности приобрести книгу")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critic')
@allure.label('layer', 'web')
def test_buy_paper_book(book_page):
    book_page.buy_paper_book_btn.click()
    book_page.page.wait_for_timeout(1000)
    close_authorization_popup(book_page.page)
    assert not book_page.is_in_cart()


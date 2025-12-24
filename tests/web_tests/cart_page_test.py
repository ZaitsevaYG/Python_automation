from playwright.sync_api import expect
from utils.utils import close_authorization_popup
import allure

@allure.epic('Взаимодействие с книгой на странице Корзины')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности переместить в отложенное и удалить книгу из корзины")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_book_to_postponed_and_delete(cart_page):
    cart_page.delete_from_cart_already_postponed_book()
    cart_page.cart_is_empty()

@allure.epic('Взаимодействие с книгой на странице Корзины')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности переместить в отложенное и удалить книгу из корзины")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_delete_and_postpone(cart_page):
    expect(cart_page.empty_heart_icon).to_be_visible(timeout=3000)
    cart_page.delete_btn.click()
    cart_page.delete_and_postpone_btn.click(timeout=3000)
    expect(cart_page.filled_heart_icon).to_be_visible(timeout=3000)
    cart_page.cart_is_empty()

@allure.epic('Взаимодействие с книгой на странице Корзины')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности удалить книгу из корзины")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_delete_from_cart(cart_page):
    cart_page.delete_btn.click()
    expect(cart_page.filled_heart_icon).not_to_be_visible()
    cart_page.delete_from_cart_popup_btn.click(timeout=3000)
    cart_page.cart_is_empty()

@allure.epic('Взаимодействие с книгой на странице Корзины')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности приобрести книгу")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_checkout_without_authorization(cart_page):
    cart_page.buy_book()
    close_authorization_popup(cart_page.page)
from playwright.sync_api import expect
import re
from utils import close_authorization_popup
import allure

@allure.epic('Взаимодействие с книгой на странице Корзины')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности переместить в отложенное и удалить книгу из корзины")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_book_to_postponed_and_delete(cart_page):
    cart_page.postpone_book()
    expect(cart_page.filled_heart_icon).to_be_visible()
    cart_page.delete_btn.click()
    expect(cart_page.delete_and_postpone_btn).not_to_be_visible()
    expect(cart_page.delete_from_cart_popup_btn).to_be_visible()
    cart_page.delete_from_cart_popup_btn.click()
    expect(cart_page.empty_cart_state).to_have_text(re.compile(r"Корзина пуста"))

@allure.epic('Взаимодействие с книгой на странице Корзины')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности переместить в отложенное и удалить книгу из корзины")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_delete_and_postpone(cart_page):
    expect(cart_page.empty_heart_icon).to_be_visible()
    cart_page.delete_btn.click()
    cart_page.delete_and_postpone_btn.click()
    expect(cart_page.filled_heart_icon).to_be_visible()
    cart_page.page.wait_for_timeout(1000)
    expect(cart_page.empty_cart_state).to_have_text(re.compile(r"Корзина пуста"))
    expect(cart_page.empty_cart_state).to_be_visible(timeout=10000)

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
    cart_page.delete_from_cart_popup_btn.click()
    cart_page.page.wait_for_timeout(5000)
    expect(cart_page.empty_cart_state).to_have_text(re.compile(r"Корзина пуста"))

@allure.epic('Взаимодействие с книгой на странице Корзины')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка возможности приобрести книгу")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_checkout_without_authorization(cart_page):
    cart_page.buy_book()
    cart_page.page.wait_for_timeout(1000)
    close_authorization_popup(cart_page.page)
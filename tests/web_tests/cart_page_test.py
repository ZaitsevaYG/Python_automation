from playwright.sync_api import expect
import re
from utils import close_authorization_popup
from pages.web_pages.cart_page import CartPage
from data.books import ATOMIC_HABITS



def test_add_book_to_postponed_and_delete(cart_page):
    #cart_page = CartPage(page, ATOMIC_HABITS)
    #cart_page.navigate_and_add_to_cart()
    cart_page.postpone_book()
    expect(cart_page.filled_heart_icon).to_be_visible()
    cart_page.delete_btn.click()
    expect(cart_page.delete_and_postpone_btn).not_to_be_visible()
    expect(cart_page.delete_from_cart_popup_btn).to_be_visible()
    cart_page.delete_from_cart_popup_btn.click()
    expect(cart_page.empty_cart_state).to_have_text(re.compile(r"Корзина пуста"))

def test_delete_and_postpone(cart_page):
    #cart_page = CartPage(page, ATOMIC_HABITS)
    #cart_page.navigate_and_add_to_cart()
    expect(cart_page.empty_heart_icon).to_be_visible()
    cart_page.delete_btn.click()
    cart_page.delete_and_postpone_btn.click()
    expect(cart_page.filled_heart_icon).to_be_visible()
    cart_page.page.wait_for_timeout(1000)
    #expect(cart_page.empty_cart_state).to_have_text(re.compile(r"Корзина пуста"))
    expect(cart_page.empty_cart_state).to_be_visible(timeout=10000)

def test_delete_from_cart(cart_page):
    # cart_page = CartPage(page, ATOMIC_HABITS)
    # cart_page.navigate_and_add_to_cart()
    cart_page.delete_btn.click()
    expect(cart_page.filled_heart_icon).not_to_be_visible()
    cart_page.delete_from_cart_popup_btn.click()
    cart_page.page.wait_for_timeout(5000)
    expect(cart_page.empty_cart_state).to_have_text(re.compile(r"Корзина пуста"))

def test_checkout_without_authorization(cart_page):
    # cart_page = CartPage(page, ATOMIC_HABITS)
    # cart_page.navigate_and_add_to_cart()
    cart_page.buy_book()
    cart_page.page.wait_for_timeout(1000)
    close_authorization_popup(cart_page.page)
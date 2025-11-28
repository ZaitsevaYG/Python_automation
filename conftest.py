import pytest

from pages.cart_page import CartPage
from pages.start_page import StartPage
from pages.book_page import BookPage


"""
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:

        browser = p.chromium.launch(
            channel="chrome",
            headless=True
        )
        page = browser.new_page()
        yield page
        browser.close() """



@pytest.fixture
def start_page(page):
    sp = StartPage(page)
    sp.navigate()
    return sp


@pytest.fixture
def book_page(page):
    bp = BookPage(page)
    bp.navigate()
    return bp

@pytest.fixture
def cart_page(page):
    cp = CartPage(page)
    cp.navigate_and_add_to_cart()
    return cp

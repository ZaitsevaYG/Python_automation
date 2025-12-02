from asyncio import timeout

import pytest

from pages.web_pages.cart_page import CartPage
from pages.web_pages.start_page import StartPage
from pages.web_pages.book_page import BookPage
from data.books import ATOMIC_HABITS



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
def start_page(browser):
    context = browser.new_context()
    page = context.new_page()
    sp = StartPage(page)
    sp.navigate()
    yield sp
    context.close()


@pytest.fixture
def book_page(browser):
    context = browser.new_context()
    page = context.new_page()
    bp = BookPage(page,ATOMIC_HABITS)
    bp.navigate()
    yield bp
    context.close()




@pytest.fixture
def cart_page(browser):
    context = browser.new_context()
    page = context.new_page()
    cp = CartPage(page, ATOMIC_HABITS)
    cp.navigate_and_add_to_cart()
    yield cp
    context.close()

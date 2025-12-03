

import pytest

from pages.web_pages.cart_page import CartPage
from pages.web_pages.start_page import StartPage
from pages.web_pages.book_page import BookPage
from data.books import ATOMIC_HABITS


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

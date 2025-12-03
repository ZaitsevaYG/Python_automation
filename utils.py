import allure
from playwright.sync_api import Page, TimeoutError, expect

def close_promo_popup(page: Page, timeout=5000):
    modal = page.locator('[data-testid="modal--wrapper"][aria-hidden="false"]')
    close_button = page.locator('[data-testid="modal__close--button"]')
    already_in_the_cart_btn = page.get_by_test_id("book__goToCartButton")

    if close_button.is_visible():
        close_button.click()
        modal.wait_for(state="hidden", timeout=timeout)
    else:

        max_retries = 3
        for attempt in range(max_retries):
            try:
                page.locator('body').click(position={"x": 10, "y": 600}, force=True)
                return
            except TimeoutError:
                if attempt == max_retries - 1:
                    raise
                print(f"Attempt {attempt + 1} failed, retrying...")
                page.wait_for_timeout(2000)



def close_authorization_popup (page: Page):
    authorization_popup = page.get_by_test_id("authorization-popup")
    close_auth_popup_btn = page.get_by_test_id("authorization-popup__close-button")
    expect(authorization_popup).to_be_visible()
    close_auth_popup_btn.click()

def allure_screenshot(page: Page):
    allure.attach(
        page.screenshot(timeout=7000),
        attachment_type=allure.attachment_type.PNG
    )
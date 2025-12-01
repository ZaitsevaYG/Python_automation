from playwright.sync_api import Page, Error, expect


def close_promo_popup(page: Page, timeout=5000):

    close_btn = page.get_by_test_id("modal__close--button")

    try:

        close_btn.wait_for(state="visible", timeout=timeout)
        close_btn.click(force=True)
        close_btn.wait_for(state="hidden", timeout=timeout)

    except Error:
        print("Попап не появился.")

def close_authorization_popup (page: Page, timeout=5000):
    authorization_popup = page.get_by_test_id("authorization-popup")
    close_auth_popup_btn = page.get_by_test_id("authorization-popup__close-button")
    expect(authorization_popup).to_be_visible()
    close_auth_popup_btn.click()
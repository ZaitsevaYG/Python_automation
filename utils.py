from playwright.sync_api import Page, Error, expect


def close_promo_popup(page: Page, timeout=5000):
    # Ищем попап где угодно на странице, но только видимый
    modal = page.locator('[data-testid="modal--wrapper"][aria-hidden="false"]')
    close_button = page.locator('[data-testid="modal__close--button"]')

    print(f"Looking for any visible popup...")
    print(f"Visible modal count: {modal.count()}")

    try:
        modal.wait_for(state="attached", timeout=timeout)

        # Проверяем, видим ли он
        if modal.is_visible():
            print("Visible popup found, attempting to close...")

            # Кликаем по кнопке закрытия
            close_button.wait_for(state="visible", timeout=timeout)
            close_button.click()

            # Ждем, пока попап исчезнет
            modal.wait_for(state="hidden", timeout=timeout)
            print("Popup closed successfully")
        else:
            print("Popup is not visible")

    except Exception as e:
        print(f"Popup not found or already closed: {str(e)}")
        pass

def close_authorization_popup (page: Page, timeout=5000):
    authorization_popup = page.get_by_test_id("authorization-popup")
    close_auth_popup_btn = page.get_by_test_id("authorization-popup__close-button")
    expect(authorization_popup).to_be_visible()
    close_auth_popup_btn.click()
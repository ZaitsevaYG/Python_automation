import logging

import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page, TimeoutError, expect

@allure.step("Закрыть поп-ап с промо '3+1'")
def close_promo_popup(page: Page, timeout=5000):
    modal = page.locator('[data-testid="modal--wrapper"][aria-hidden="false"]')
    close_button = page.locator('[data-testid="modal__close--button"]')


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


@allure.step("Закрыть авторизационный поп-ап")
def close_authorization_popup (page: Page):
    authorization_popup = page.get_by_test_id("authorization-popup")
    close_auth_popup_btn = page.get_by_test_id("authorization-popup__close-button")
    expect(authorization_popup).to_be_visible()
    close_auth_popup_btn.click()


@allure.step("Сделать скриншот")
def allure_screenshot(page: Page):
    try:

        screenshot = page.screenshot(timeout=7000, type='jpeg')
        allure.attach(
            screenshot,
            name="Скриншот страницы",
            attachment_type=allure.attachment_type.JPG
        )
    except Exception as e:
        logging.warning(f"Не удалось сделать скриншот: {e}")

        allure.attach(
            f"Ошибка при создании скришота: {e}".encode(),
            name="Ошибка скриншота",
            attachment_type=allure.attachment_type.TEXT
        )


def allure_add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def allure_add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def allure_add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video', AttachmentType.HTML, '.html')
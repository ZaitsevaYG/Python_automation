import os

from pathlib import Path
import allure
import allure_commons
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser, support


# def to_driver_options(context):
#     options = UiAutomator2Options()
#
#     if context == 'local_emulator':
#         options.set_capability('remote_url', os.getenv('REMOTE_URL'))  # адрес удаленного сервера
#         options.set_capability('deviceName', os.getenv('DEVICE_NAME'))  # имя устройства
#         options.set_capability('appWaitActivity', os.getenv(
#             'APP_WAIT_ACTIVITY'))  # активити, которая будет открыта после запуска apk файла
#         # options.set_capability('udid', os.getenv('UDID')) # уникальный идентификатор устройства
#         options.set_capability('app', utils.file.abs_path_from_project(os.getenv('APP')))  # путь до apk файла
#
#     if context == 'local_real_device':
#         options.set_capability('remote_url', os.getenv('REMOTE_URL'))
#         options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
#         options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
#         # options.set_capability('udid', os.getenv('UDID'))
#         options.set_capability('app', utils.file.path_from_project(os.getenv('APP')))
#
#     return options

apk_path = Path(__file__).parent.parent.parent / 'data' / 'Litres.apk'

if not apk_path.exists():
    raise FileNotFoundError(f"APK file not found at: {apk_path}")

@pytest.fixture(scope='function', autouse=True)
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "deviceName": "JMS_L09",
        "appActivity": "ru.litres.android.splash.SplashActivity",
        "appPackage": "ru.litres.android.international",
        "app": str(apk_path)
    })

    browser.config.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=options
    )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )


    try:

        browser.element((AppiumBy.ID, "ru.litres.android.international:id/choosebutton")).click()
        browser.element((AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")).click()
    except Exception:
        pass

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    with allure.step('tear down app session'):
        browser.quit()

from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy


class AndroidAccountPage:

    def change_color_theme(self):
        browser.element((AppiumBy.XPATH, "(//android.widget.LinearLayout[@resource-id='ru.litres.android.international:id/navigation_bar_item_content_container'])[5]")).click()
        browser.element((AppiumBy.XPATH,
                         "//android.widget.TextView[@resource-id='ru.litres.android.international:id/spinner_name' and @text='Тёмная тема']")).click()
        browser.element((AppiumBy.XPATH, "//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Включена']")).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.Button")).click()

        return self

    def check_dark_theme_on(self):
        browser.element((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="ru.litres.android.international:id/spinner_value" and @text="Включена"]')).should(have.text("Включена"))
        return self

    def change_adult_content(self):
        browser.element((AppiumBy.XPATH,
                         "(//android.widget.LinearLayout[@resource-id='ru.litres.android.international:id/navigation_bar_item_content_container'])[5]")).click()
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Ограничение взрослого контента"))')).click()
        browser.element((AppiumBy.XPATH,
                       "//android.widget.CheckedTextView[@resource-id=\'android:id/text1' and @text='Выключено']")).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.Button")).click()

        return self

    def check_adult_content_on(self):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="ru.litres.android.international:id/spinner_value" and @text="Выключено"]')).should(
            have.text("Выключено"))
        return self

account_page = AndroidAccountPage()
import allure
from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy


class AndroidAccountPage:

    @allure.step('Перейти в меню пользователя, нажать на элемент "Темная тема" -> "Включена"')
    def change_color_theme(self):
        browser.element((AppiumBy.XPATH, "(//android.widget.LinearLayout[@resource-id='ru.litres.android.international:id/navigation_bar_item_content_container'])[5]")).click()
        browser.element((AppiumBy.XPATH,
                         "//android.widget.TextView[@resource-id='ru.litres.android.international:id/spinner_name' and @text='Тёмная тема']")).click()
        browser.element((AppiumBy.XPATH, "//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='Включена']")).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.Button")).click()

        return self

    @allure.step('Проверка, что темная тема включена на устройстве')
    def check_dark_theme_on(self):
        browser.element((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="ru.litres.android.international:id/spinner_value" and @text="Включена"]')).should(have.text("Включена"))
        return self

    @allure.step('Перейти в меню пользователя, нажать на элемент "Язык интерфейса" -> "English"')
    def change_language(self):
        browser.element((AppiumBy.XPATH,
                         "(//android.widget.LinearLayout[@resource-id='ru.litres.android.international:id/navigation_bar_item_content_container'])[5]")).click()

        browser.element((AppiumBy.XPATH,
                         "//android.widget.TextView[@resource-id='ru.litres.android.international:id/spinner_name' and @text='Язык интерфейса']")).click()
        browser.element((AppiumBy.XPATH,
                       "//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='English']")).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.Button")).click()

        return self

    @allure.step('Проверка, что применилось изменение языка на английский')
    def check_language_change(self):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="ru.litres.android.international:id/spinner_value" and @text="English"]')).should(
            have.text("English"))
        browser.element((AppiumBy.ID,"ru.litres.android.international:id/tv_config")).should(have.text("Settings"))
        return self

account_page = AndroidAccountPage()
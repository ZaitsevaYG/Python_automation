import allure

from pages.mobile_pages_android.account_page_app import account_page


@allure.epic('Настройки аккаунта')
@allure.label("owner", "Zaitseva Yana")
@allure.feature("Проверка смены темы на темную в мобильном приложении")
@allure.severity('normal')
@allure.label('layer', 'mobile')

def test_change_color_theme(android_mobile_management):
    account_page.change_color_theme()
    account_page.check_dark_theme_on()



@allure.epic('Настройки аккаунта')
@allure.label("owner", "Zaitseva Yana")
@allure.feature("Проверка смены языка в приложении")
@allure.severity('normal')
@allure.label('layer', 'mobile')

def test_change_language(android_mobile_management):
    account_page.change_language()
    account_page.check_language_change()
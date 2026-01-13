<h1> Проект по тестированию сервиса электронных и аудиокниг "Литрес"</h1>

> <a target="_blank" href="https://www.litres.ru">Ссылка на сайт</a>

![This is an image](data/rm_design/Litres_page.png)

<h3> Список проверок, реализованных в автотестах:</h3>

### UI-тесты

- [x] Поиск книги
- [x] Добавление книги в корзину
- [x] Удаление книги из корзины
- [x] Добавление книги в Избранное
- [x] Удаление книги из Избранного
- [x] Проверка элементов на странице книги
- [x] Проверка элементов на странице "Мои книги"

### API-тесты

- [x] Поиск книги
- [x] Добавление книги в корзину
- [x] Попытка авторизации незарегистрированным пользователем

### Mobile-тесты
- [x] Поиск книги(успешный и неуспешный)
- [x] Добавление книги в Сохраненное
- [x] Удаление книги из Сохраненного
- [x] Смена цветовой темы приложения
- [x] Изменение языка интерфейса

----
### Проект реализован с использованием:
<img src="data/rm_design/icons/python-original.svg" width="50"> <img src="data/rm_design/icons/pytest.png" width="50"> <img src="data/rm_design/icons/intellij_pycharm.png" width="50"> <img src="data/rm_design/icons/selene.png" width="50"> <img src="data/rm_design/icons/playwright_logo.png" width="50"> <img src="data/rm_design/icons/jenkins.png" width="50"> <img src="data/rm_design/icons/allure_report.png" width="50"> <img src="data/rm_design/icons/appium_logo.png" width="50"> <img src="data/rm_design/icons/android_logo.png" width="50">

----
### Локальный запуск
> Для локального запуска с дефолтными значениями необходимо выполнить команду:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests
```

----
### Удаленный запуск автотестов выполнялся на сервере Jenkins, поднятом локально

![This is an image](data/rm_design/Jenkins_tests.png)

----
### Allure отчет
#### Общие результаты
![This is an image](data/rm_design/allure.png)

#### Список тест кейсов
![This is an image](data/rm_design/test_cases.png)
#### Пример отчета о прохождении ui-теста
![This is an image](data/rm_design/ui_test.png)
#### Пример отчета о прохождении api-теста
![This is an image](data/rm_design/api_test.png)

Мобильное тестирование в данном проекте реализовано на реальном девайсе на платформе Android.  
Для прогона локально тестов необходимо скачать и положить в папку data  <a href="https://drive.google.com/uc?export=download&id=1qAgPymonfSuqqg6CyYDRi-62NJxYD-Uh">apk файл</a>.

#### Пример отчета о прохождении mobile-теста
![This is an image](data/rm_design/allure_mobile.png)

### Пример видео прохождения mobile-автотестoв
![autotest_gif](data/rm_design/mobile-tests-video.gif)

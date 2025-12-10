import allure
import jsonschema

from utils.api_req import api_get
from utils.load_schema import load_schema


@allure.epic('API. Поиск книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка поиска книги с главной страницы")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_successful_searching_of_book_by_title():
    schema = load_schema('book_search_success.json')

    book_title = 'Герои книг на приеме у психотерапевта'
    art_types = 'text_book'
    types = 'text_book'
    url = f"/search?q={book_title}&art_types={art_types}&types={types}"
    headers = {"Content-Type": "application/json"}

    result = api_get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['payload']['data'][0]['type'] == "text_book"
    assert result.json()['payload']['data'][0]['instance']['art_type'] == 0
    assert 'Герои книг на приеме у психотерапевта' in result.json()['payload']['data'][0]['instance']['title']


@allure.epic('API. Поиск книги')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка поиска книги с главной страницы")
@allure.label('microservice', 'API')
@allure.label('microservice', 'Search')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_unsuccessful_searching_of_book_by_title():
    schema = load_schema('book_search_unsuccess.json')

    book_title = 'fyktjurheird'
    types = 'text_book'
    url = f"/search?q={book_title}&types={types}"
    headers = {"Content-Type": "application/json"}

    result = api_get(url, headers=headers)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert len(result.json()['payload']['data']) == 0
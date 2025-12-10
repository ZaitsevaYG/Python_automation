import allure
import jsonschema

from utils.api_req import api_put
from utils.load_schema import load_schema


@allure.epic('API. Добавление книги в корзину')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка добавления книги в корзину через API")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_adding_book_to_cart():
    schema = load_schema('add_book_to_cart.json')

    url = "/cart/arts/add"
    art_ids = [64353482]
    headers = {"Content-Type": "application/json"}

    result = api_put(url, headers=headers, json={"art_ids": art_ids})

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()['payload']['data']['added_art_ids'] == art_ids
    assert result.json()['payload']['data']['failed_art_ids'] == []
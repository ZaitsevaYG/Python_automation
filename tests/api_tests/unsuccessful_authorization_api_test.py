
import allure
import jsonschema

from utils.api_req import api_post
from utils.load_schema import load_schema


@allure.epic('API. Незарегистрированный пользователь. Авторизация')
@allure.label("owner", "Yana Zaitseva")
@allure.feature("Проверка ответа системы на попытку авторизации незарегистрированного пользователя")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
def test_authorization_unregistered_user():
    schema = load_schema('auth_unsuccessful.json')

    url = "/auth/login"
    email = "no_user@mail.de"
    invalid_password = "TrustNo1"
    headers = {"Content-Type": "application/json"}

    result = api_post(url, headers=headers, json={"login": email, "password": invalid_password})

    assert result.status_code == 401
    jsonschema.validate(result.json(), schema)
    assert result.json()['error']['type'] == "Unauthorized"
    assert result.json()['error']['title'] == "Incorrect user data"
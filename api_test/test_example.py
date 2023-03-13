import pytest
import requests

class TestExample:
    names = [
        ("Vitalii"),
        ("Serj"),
        ("Nastya"),
        (""),
        ("123#%#%")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong status code"

        response_dict = response.json()
        assert "answer" in response_dict, f"There is no field 'answer' in the response"

        if len(name) == 0:
            expected_response = "Hello, someone"
        else:
            expected_response = f"Hello, {name}"
            actual_response = response_dict["answer"]
            assert actual_response == expected_response, "Actual text in the response is incorrect"

import json
import requests


class API:
    def verify_api(self):
        pet = {"id": 1, "breed": "String", "age": 0}
        response1 = requests.post(url='https://petstore.swagger.io/v2/pet', json=pet)
        response1_json = response1.json()

        response2 = requests.get(url='https://petstore.swagger.io/v2/pet/1')
        response2_json = response2.json()

        response3 = requests.delete('https://petstore.swagger.io/v2/pet/1')
        response3_json = response3.json()

        assert response1.status_code == 200
        assert response2.status_code == 200
        assert response3.status_code == 200
        # print(response1_json, response2_json, response3_json)



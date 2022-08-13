import json
import requests


class API:
    def verify_api_1(self):
        pet = {"id": 1, "name": "Rex", "photoUrls": ['string'], 'tags': [], "status": "ready"}
        response1 = requests.post(url='https://petstore.swagger.io/v2/pet', json=pet)
        response1_json = response1.json()

        response2 = requests.get(url='https://petstore.swagger.io/v2/pet/1')
        response2_json = response2.json()

        response3 = requests.delete('https://petstore.swagger.io/v2/pet/1')
        response3_json = response3.json()

        print(response1_json, response2_json, response3_json)
        assert response1.status_code == 200
        assert response2.status_code == 200
        assert response3.status_code == 200
        assert response2_json['status'] == 'ready'



    def verify_api_2(self):
        user = {
            "id": 2,
            "username": "Dima",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 2
        }
        user2 = {
            "id": 2,
            "username": "Vitaliy",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 2
        }
        response4 = requests.post(url='https://petstore.swagger.io/v2/user', json=user)
        response4_json = response4.json()

        response5 = requests.get(url='https://petstore.swagger.io/v2/user/Dima')
        response5_json = response5.json()
        # response5_json_username = response5_json['username']

        response6 = requests.put(url='https://petstore.swagger.io/v2/user/Dima', json=user2)
        response6_json = response6.json()

        response7 = requests.get(url='https://petstore.swagger.io/v2/user/Vitaliy')
        response7_json = response7.json()
        # response7_json_username = response7_json['username']

        print(response4_json, response5_json, response6_json, response7_json, response5_json['username'], response7_json['username'])
        assert response4.status_code == 200
        assert response5.status_code == 200
        assert response6.status_code == 200
        assert response7.status_code == 200
        assert response5_json['username'] != response7_json['username']


abc = API()
abc.verify_api_1()


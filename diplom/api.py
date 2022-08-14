import requests


class API:
    def __init__(self, get_user_data_json=None):
        self.get_user_data_json = None

    def add_new_pet(self):
        pet = {"id": 1, "name": "Rex", "photoUrls": ['string'], 'tags': [], "status": "ready"}
        add_new_pet = requests.post(url='https://petstore.swagger.io/v2/pet', json=pet)
        add_new_pet_json = add_new_pet.json()
        assert add_new_pet.status_code == 200, f"status_code should be equal 200, got {add_new_pet.status_code} instead. Received json: {add_new_pet_json}"

    def check_new_pet(self):
        check_new_pet = requests.get(url='https://petstore.swagger.io/v2/pet/1')
        check_new_pet_json = check_new_pet.json()
        assert check_new_pet.status_code == 200, f"status_code should be equal 200, got {check_new_pet.status_code} instead. Received json: {check_new_pet_json}"
        assert check_new_pet_json['status'] == 'ready', f"check_new_pet_json['status'] should be equal 'ready', got {check_new_pet_json['status']} instead."

    def delete_new_pet(self):
        delete_new_pet = requests.delete('https://petstore.swagger.io/v2/pet/1')
        delete_new_pet_json = delete_new_pet.json()
        assert delete_new_pet.status_code == 200, f"status_code should be equal 200, got {delete_new_pet.status_code} instead. Received json: {delete_new_pet_json}"

        # print(add_new_pet_json, check_new_pet_json, delete_new_pet_json)
        # assert add_new_pet.status_code == 200, f"status_code should be equal 200, got {add_new_pet.status_code} instead. Received json: {add_new_pet_json}"
        # assert check_new_pet.status_code == 200, f"status_code should be equal 200, got {check_new_pet.status_code} instead. Received json: {check_new_pet_json}"
        # assert delete_new_pet.status_code == 200, f"status_code should be equal 200, got {delete_new_pet.status_code} instead. Received json: {delete_new_pet_json}"
        # assert check_new_pet_json['status'] == 'ready', f"check_new_pet_json['status'] should be equal 'ready', got {check_new_pet_json['status']} instead."

    def create_user(self):
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

        create_user = requests.post(url='https://petstore.swagger.io/v2/user', json=user)
        create_user_json = create_user.json()
        assert create_user.status_code == 200, f"create_user status_code should be equal 200, got {create_user.status_code} instead. Received json: {create_user_json}"

    def get_user_data(self):
        get_user_data = requests.get(url='https://petstore.swagger.io/v2/user/Dima')
        self.get_user_data_json = get_user_data.json()
        assert get_user_data.status_code == 200, f"get_user_data status_code should be equal 200, got {get_user_data.status_code} instead. Received json: {self.get_user_data_json}"

    def change_user_name(self):
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
        change_user_name = requests.put(url='https://petstore.swagger.io/v2/user/Dima', json=user2)
        change_user_name_json = change_user_name.json()
        assert change_user_name.status_code == 200, f"change_user_name status_code should be equal 200, got {change_user_name.status_code} instead. Received json {change_user_name_json}"

    def check_user_name(self):
        check_user_name = requests.get(url='https://petstore.swagger.io/v2/user/Vitaliy')
        check_user_name_json = check_user_name.json()
        assert check_user_name.status_code == 200, f"check_user_name status_code should be equal 200, got {check_user_name.status_code} instead. Received json {check_user_name_json}"
        assert self.get_user_data_json['username'] != check_user_name_json['username'], f"{self.get_user_data_json['username']} should not be equal {check_user_name_json['username']}."

        # print(create_user_json, get_user_data_json, change_user_name_json, check_user_name_json, get_user_data_json['username'], check_user_name_json['username'])
        # assert create_user.status_code == 200, f"create_user status_code should be equal 200, got {create_user.status_code} instead. Received json: {create_user_json}"
        # assert get_user_data.status_code == 200, f"get_user_data status_code should be equal 200, got {get_user_data.status_code} instead. Received json: {get_user_data_json}"
        # assert change_user_name.status_code == 200, f"change_user_name status_code should be equal 200, got {change_user_name.status_code} instead. Received json {change_user_name_json}"
        # assert check_user_name.status_code == 200, f"check_user_name status_code should be equal 200, got {check_user_name.status_code} instead. Received json {check_user_name_json}"
        # assert get_user_data_json['username'] != check_user_name_json['username'], f"{get_user_data_json['username']} should not be equal {check_user_name_json['username']}."

import requests


class APIClient:
    BASE_URL = "https://reqres.in/api"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": "reqres-free-v1",
        }

    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def put(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, headers=self.headers, json=data)
        return response

    def patch(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.patch(url, headers=self.headers, json=data)
        return response

    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, headers=self.headers)
        return response

import requests

class Calculator:
    
    def add(self, a, b):
        return a + b

    def get_random_number(self):
        response = requests.get("https://randomapi.com/api/random")
        if response.status_code == 200:
            return response.json()['number']
        else:
            return None

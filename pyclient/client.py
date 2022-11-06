import requests, json

endpoint = "http://localhost:8000/api/home/"

response = requests.get(endpoint)

try:
    print(response.json())
except:
    print("Except : ", response)
import requests

headers = {'Authorization': 'AUTH_TOKEN'}
response = requests.get(
    'API_URL', headers=headers)

payments = response.json()
print(payments)

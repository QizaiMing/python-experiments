import csv
import requests

headers = {"Authorization": "AUTH_TOKEN"}

with open("databaseClients.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar=",")
    for row in reader:
        payload = {"name": row[0], "phone": row[1]}
        response = requests.post(
            "API_URL",
            headers=headers,
            data=payload,
        )
        client = response.json()
        print(client)

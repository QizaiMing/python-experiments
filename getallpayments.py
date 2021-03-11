import requests
import csv

headers = {"Authorization": "AUTH_TOKEN"}
response = requests.get("API_URL", headers=headers)

payments = response.json()

with open("pagos.csv", "w", newline="") as csvfile:
    writer = csv.writer(
        csvfile, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL
    )
    writer.writerow(
        ["Nombre", "Telefono", "Metodo", "Direccion", "Referencia", "Monto", "Fecha"]
    )
    for payment in payments:
        writer.writerow(
            [
                payment["client_name"],
                payment["client_phone"],
                payment["method"],
                payment["location"],
                payment["transaction_number"],
                payment["amount"],
                payment["date"],
            ]
        )

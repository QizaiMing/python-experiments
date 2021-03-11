import csv

output = []

with open("sanitizedClients.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar=",")
    for row in reader:
        if row[1][0] == "4":
            output.append([row[0], f"0{row[1]}".replace("-", "")])
        else:
            output.append([row[0], row[1].replace("-", "")])

for client in output:
    print(client)

with open("databaseClients.csv", "w", newline="") as csvfile:
    writer = csv.writer(
        csvfile, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL
    )
    for client in output:
        writer.writerow([client[0], client[1]])

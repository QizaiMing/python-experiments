import csv
with open('FILENAME', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Nombre', 'Telefono', 'Metodo',
                         'Direccion', 'Referencia', 'Monto', 'Fecha'])
    for i in range(10):
        spamwriter.writerow(['Juan Chacon', '04247754975', 'Efectivo',
                             'Urb Alcaravan', '', '5USD y 35000COP', '2020-12-19'])

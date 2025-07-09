import csv

serial_number = []

with open("tagss.csv", newline='', encoding="utf-8") as arquivocsv:
    reader = csv.DictReader(arquivocsv)
    for row in reader:
        serial_number.append(row["Serial"].strip())

print("Quantidade de tags:", len(serial_number))
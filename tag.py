import requests
import csv

urlbase = "https://api.sevenseguros.com.br/"
rota_login = "login"
rota_tag = "cancel-tag/"
login_data = {
  "username": "higor.carvalho@sevenseguros.com.br",
  "password": "298689"
}
serial_number =[]

with open("tagss.csv", newline='', encoding="utf-8") as arquivocsv:
    reader = csv.DictReader(arquivocsv)
    for row in reader:
        serial_number.append(row["Serial"].strip())

print("Quantidade de tags:", len(serial_number))

motivo_cancelamento = {
  "motive": "perda/extravio"
}

acesso_login = requests.post(f"{urlbase}{rota_login}", json = login_data)

if acesso_login.status_code == 200:
    token = acesso_login.json().get("token")
else:
    print("Token não localizado")
    print("Status Code:", acesso_login.status_code)
    print("Resposta:", acesso_login.text)
    
headers = {
        "Authorization":token,
        "Content-Type": "application/json"
    }


for tag in serial_number:
    cancelamento = f"{urlbase}{rota_tag}{tag}"
    acesso_cancelamento = requests.post(cancelamento, headers=headers, json=motivo_cancelamento)
    
    if acesso_cancelamento.status_code == 200:
        print(f"tag {tag} , cancelada")
    else:
            print(f"Erro ao cancelar a tag {tag}: {acesso_cancelamento.status_code} - {acesso_cancelamento.text}")
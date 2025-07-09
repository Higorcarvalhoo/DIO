# Entrada do usuário
email = input().strip()
lista_email = list(email)


# TODO: Verifique as regras do e-mail:


if email.startswith("@") or email.endswith("@"): #Não pode começar ou terminar com "@".
    print("E-mail inválido")
else:
    if "@" not in lista_email: #Deve conter o caractere "@"
        print("E-mail inválido")
    else:
        if " " in lista_email: #Não pode conter espaços.
            print("E-mail inválido")
        else:
            print("E-mail válido")

    

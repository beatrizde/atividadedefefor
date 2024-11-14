sexo = input("Digite F para feminino e M para masculino: ")

# if sexo=="F" or sexo =="f":
#     print("Feminino")
# elif sexo == "M" or sexo == "m":
#     print("Masculino")
# else:
#     print("Sexo inválido")

# O comando lower() converte as letras para minúsculas
# O comando upper() converte as letras para maiúsculas
sexo = sexo.lower()
if sexo == "f":
    print("Feminino")
elif sexo == "m":
    print("Masculino")
else:
    print("Sexo inválido")

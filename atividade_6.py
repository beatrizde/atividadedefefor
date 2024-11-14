periodo = input("Digite M-Matutino, V-Vespertino ou N-Noturno ")
periodo = periodo.lower()

if periodo == "m":
    print("Bom dia!")
elif periodo == "v":
    print("Boa tarde!")
elif periodo == "n":
    print("Boa noite!")
else:
    print("Valor inválido!")

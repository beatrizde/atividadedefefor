# Exercício 1 de funções
def soma(numero1,numero2):
    return numero1 + numero2

# Exercício 2 de funções
def converterCelFah(tempCelsius):
    fah = 1.8 * tempCelsius + 32
    return fah

# Execício 3 de funções
def parImpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

# Execício 4 de funções
def inverter(texto):
    tam = len(texto)
    #criar variável que devolve o texto invertido
    txt_invertido=""
    for i in range(tam-1,-1,-1):
        txt_invertido += texto[i]
    return txt_invertido

# Exercício 5 de funções
def palindromo(palavra):
    palavra = palavra.lower()
    cp_palavra = palavra
    if cp_palavra==inverter(palavra):
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"
    
# Execício 6 de funções
def media(lista_numeros):
    resultado = 0
    for i in lista_numeros:
        resultado += i
    return resultado / len(lista_numeros)

# Execício 7 de funções
def lista_pares(lista_numeros):
    lst_pares = []
    for i in lista_numeros:
        if i % 2 == 0:
            lst_pares.append(i)
    return lst_pares
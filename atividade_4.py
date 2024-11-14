letra = input("Digite uma letra ")

if letra=='a' or letra=='A':
    print("A letra digitada é uma vogal")
    
elif letra == 'e' or letra == 'E':
    print("A letra digitada é uma vogal")
    
elif letra == 'i' or letra == 'I':
    print("A letra digitada é uma vogal")
    
elif letra == 'o' or letra == 'O':
    print("A letra digitada é uma vogal")
    
elif letra == 'u' or letra == 'U':
    print("A letra digitada é uma vogal")
    
else:
    print("A letra digitada é uma consoante")


letra = letra.lower()

if letra == 'a' or letra =='e' or letra =='i' or letra=='o'  or letra=='u':
    print("A letra digitada é uma vogal")
else:
    print("A letra digitada é uma consoante")
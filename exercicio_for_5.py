bs = int(input("Digite um valor para a base "))
ex = int(input("Digite um valor para expoente "))

n = bs
for i in range(0,ex-1):
    n = n * bs
    
print("O resultado da potência é "+str(n))

str
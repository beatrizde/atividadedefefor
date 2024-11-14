texto = "Quinta"
# #   Q u i n t a
# #-1 0 1 2 3 4 5
tm = len(texto)
# print(tm)
# print(texto[0])
# print(texto[5])
# print(texto[6-1])
# print(texto[tm-1])



for i in range(tm-1,-1,-1):
    print(texto[i],end="")

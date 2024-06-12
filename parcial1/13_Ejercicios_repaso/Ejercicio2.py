lista = []


valor = 1  
while len(lista) < 120:
    lista.append(valor)
    valor += 1  

print("Lista con valores añadidos:")
for numero in lista:
    print(numero)
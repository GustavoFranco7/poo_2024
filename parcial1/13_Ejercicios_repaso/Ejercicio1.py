def mostrar_lista(lista):
    print("Lista de números:")
    for numero in lista:
        print(numero, end=" ")
    print()

def lista_a_string(lista):
    return ' '.join(str(numero) for numero in lista)

def buscar_elemento(lista, elemento):
    if elemento in lista:
        return f"El elemento {elemento} está en la lista."
    else:
        return f"El elemento {elemento} no está en la lista."


numeros = [4, 8, 2, 10, 6, 1, 9, 5]


mostrar_lista(numeros)

cadena_numeros = lista_a_string(numeros)
print("La lista como string:", cadena_numeros)

numeros.sort()
mostrar_lista(numeros)

print("Longitud de la lista:", len(numeros))

elemento_buscar = int(input("Ingrese el número que desea buscar: "))
print(buscar_elemento(numeros, elemento_buscar))
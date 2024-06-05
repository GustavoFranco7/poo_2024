"""

    List (Array)
    son colecciones o conjuntos de datos/valores bajo 
    un mismo nombre para acceder a los valores se hace con un indice numerico

    Nota: sus valores si son modificables

    La lista es una coleccion ordenada y modificable. Permite miembros duplicados

"""

#Ejemplo 1 crear una lista con valores enteros e imprimir la lista
"""
numeros=[23,34]
print(numeros)

#recorrer la lista con un for
for i in numeros:
    print(i)

#recorrer la lista con un while
i=0
while i<len(numeros): 
    print(numeros[1])
    i+=1
"""
#Ejemplo 2 crear una lista de palabras posteriormente ingresar una palabra para buscar la coincidencia
#en la lista e indicar si aparece la palabra y en que posicion en caso contrario indicar
#una sola vez si no la encontro


palabras = ["hola", "2024", "10.23", "true"]

palabra_buscar = input("Ingrese la palabra a buscar: ")

if palabra_buscar in palabras:
    posicion = palabras.index(palabra_buscar)
    print(f"Encontre la palabra {palabra_buscar} en la posición {posicion}.")
else:
    print(f"La palabra '{palabra_buscar}' no se encontró en la lista.")





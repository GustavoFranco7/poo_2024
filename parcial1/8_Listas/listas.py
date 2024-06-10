# """

#     List (Array)
#     son colecciones o conjuntos de datos/valores bajo 
#     un mismo nombre para acceder a los valores se hace con un indice numerico

#     Nota: sus valores si son modificables

#     La lista es una coleccion ordenada y modificable. Permite miembros duplicados

# """

# #Ejemplo 1 crear una lista con valores enteros e imprimir la lista
# """
# numeros=[23,34]
# print(numeros)

# #recorrer la lista con un for
# for i in numeros:
#     print(i)

# #recorrer la lista con un while
# i=0
# while i<len(numeros): 
#     print(numeros[1])
#     i+=1
# """
#Ejemplo 2 crear una lista de palabras posteriormente ingresar una palabra para buscar la coincidencia
#en la lista e indicar si aparece la palabra y en que posicion en caso contrario indicar
#una sola vez si no la encontro


# palabras = ["hola", "2024", "10.23", "true"]

# palabra_buscar = input("Ingrese la palabra a buscar: ")

# if palabra_buscar in palabras:
#    posicion = palabras.index(palabra_buscar)
#    print(f"Encontre la palabra '{palabra_buscar}' en la posición {posicion}.")
# else:
#     print(f"La palabra '{palabra_buscar}' no se encontró en la lista.")

#Ejemplo 3 crear una lista multilinea o multidimensional (matriz) para crear una agenda telefonica

# agenda=[
#     ["Carlos", 618123456],
#     ["Fernando", 618233456],
#     ["Matias",6691112221],
#     ["Juan",6182332345],
# ]
# #print (agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}")

#Ejemplo 4 crear un programa que permita gestionar peiliculas, colocar un menu de opciones para agregar, remover, consultar peliculas
#notas:
#1- Utilizar funciones y mandar llamar de otro archivo
#2- Utilizar listas para almacenar los nombres de las peliculas
def insertarpeliculas():
    pelicula=input("ingrese la pelicula")
    peliculas.append(pelicula)
    esperetecla()
def removerpeliculas():
    pelicula=input("ingrese la pelicula")
    peliculas.remove(pelicula)
    esperetecla()



peliculas=[]
print("\n...:::CINEMEX CLON:::...\n 1-Agregar\n 2-Remover \n 3-consultar\n 4-salir")
opcion=input("\tElige una opcion").upper()

if opcion == '1' or opcion == "AGREGAR":
    insertarpeliculas()
elif opcion == '2' or opcion == "REMOVER":
    removerpeliculas()






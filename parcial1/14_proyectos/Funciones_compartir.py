lista_peliculas = ["Toy story", "cars"]

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def añadirPeliculas(): #1
    pelicula = input("Inserte nombre de la pelicula: \n")
    if pelicula in lista_peliculas:
        print("La pelicula ya está dentro del sistema")
    else:
        lista_peliculas.append(pelicula)
        print("Pelicula añadida con éxito")
    esperar_tecla()
   
def remover_pelicula(): #2
    pelicula = input("Pelicula a remover: ")
    seguro = input("¿Desea remover la pelicula? SI/NO\n").upper()
    if seguro == "SI":
        if pelicula in lista_peliculas:
            lista_peliculas.remove(pelicula)
            print(f"¡{pelicula} ha sido removida de la lista de películas!")
        else:
            print(f"{pelicula} no se encuentra en la lista de películas.")
    esperar_tecla()

def repertorio(): #4
    print("Peliculas en el repertorio:")
    for pelicula in lista_peliculas:
        print(pelicula)
    esperar_tecla()

def salir(): #7
    print("Saliendo del sistema")
    esperar_tecla()

def remplazar(): #3
    peli = input("Inserte pelicula a reemplazar: ")
    if peli in lista_peliculas:
        indice = lista_peliculas.index(peli)
        remplazo = input(f"Añadir el reemplazo de {peli}: ")
        decision = input(f"¿Estás seguro de reemplazar {peli} por {remplazo}? (S/N)").upper()
        if decision == "S" or decision == "SI":
            lista_peliculas[indice] = remplazo
            print("Lista actualizada")
        else:
            print("Cambio no hecho \n Volviendo al menú")
            esperar_tecla()
    else:
        print(f"{peli} no fue encontrada en el sistema")

def vaciar_repertorio(): #6
    lista_peliculas.clear()
    print("El repertorio ha sido vaciado.")
    esperar_tecla()

def esperar_tecla():
    input("Presiona cualquier tecla para continuar...")



def reemplazar_dato(lista, valor_a_buscar):
    # Verificar si el valor existe en la lista
    if valor_a_buscar in lista:
        # Obtener el índice del valor a buscar
        indice = lista.index(valor_a_buscar)
        
        # Solicitar al usuario el nuevo valor
        nuevo_valor = input(f"Ingresa el nuevo valor para reemplazar {valor_a_buscar}: ")
        
        # Reemplazar el valor en la lista
        lista[indice] = nuevo_valor
        print("Lista actualizada:", lista)
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la lista.")

# Lista de ejemplo
mi_lista = [1, 2, 3, 4, 5]

# Buscar y reemplazar el valor
valor_a_buscar = int(input("Ingresa el valor que quieres buscar y reemplazar en la lista: "))
reemplazar_dato(mi_lista, valor_a_buscar)

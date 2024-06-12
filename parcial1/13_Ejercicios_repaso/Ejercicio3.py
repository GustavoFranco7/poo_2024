lista = []

if not lista:
    print("La lista está vacía. Por favor, añada palabras o frases.")

    while True:
        entrada = input("Ingrese una palabra o frase (o 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        lista.append(entrada)

print("\nContenido de la lista en mayúsculas:")
for elemento in lista:
    print(elemento.upper())
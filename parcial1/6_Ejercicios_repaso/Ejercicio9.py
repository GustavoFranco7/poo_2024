#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa


while True:
    numero = int(input("Introduce un número (111 para salir): "))
    if numero == 111:
        print("¡Has introducido el 111! Saliendo del programa...")
        break
    else:
        print(f"Has introducido el número {numero}. Intenta de nuevo.")

import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

def raiz(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Raíz cuadrada de un número negativo no permitida."

def potencia(a, b):
    return a ** b

def calculadora():
    while True:
        print("Calculadora básica \n")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Raíz")
        print("6. Potencia")
        print("7. Salir \n")
        eleccion = input("Elige la operación que quieres realizar: ")

        if eleccion in ["1", "2", "3", "4", "6"]:
            n1 = float(input("Introduce el primer número: "))
            n2 = float(input("Introduce el segundo número: "))

            if eleccion == "1":
                print(f"{n1} + {n2} = {sumar(n1, n2)}")
            elif eleccion == "2":
                print(f"{n1} - {n2} = {restar(n1, n2)}")
            elif eleccion == "3":
                print(f"{n1} * {n2} = {multiplicar(n1, n2)}")
            elif eleccion == "4":
                print(f"{n1} / {n2} = {dividir(n1, n2)}")
            elif eleccion == "6":
                print(f"{n1} ^ {n2} = {potencia(n1, n2)}")
        elif eleccion == "5":
            n1 = float(input("Introduce el número para calcular la raíz cuadrada: "))
            print(f"Raíz cuadrada de {n1} = {raiz(n1)}")
        elif eleccion == "7":
            print("Programa finalizado")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

calculadora()
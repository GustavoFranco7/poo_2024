#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario


# Solicitar al usuario que ingrese dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))


if numero1 > numero2:
    numero1, numero2 = numero2, numero1


print("Números impares entre", numero1, "y", numero2, "son:")
for num in range(numero1 + 1, numero2):
    if num % 2 != 0:
        print(num)

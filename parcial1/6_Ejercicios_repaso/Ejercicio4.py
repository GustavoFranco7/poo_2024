#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado

num1 = input ("ingresa un numero ")
num2 = input ("ingresa otro numero ")

print ("suma")
suma = int(num1) + int(num2)
print (f"la suma es {suma}")


print ("resta")
resta = int(num1) - int(num2)
print (f"la resta es {resta}")

print ("multiplicacion")
multi = int(num1) * int(num2)
print (f"la multiplicacion es {multi}")

print ("division")
divi = int(num1) / int(num2)
print (f"la division es {divi}")
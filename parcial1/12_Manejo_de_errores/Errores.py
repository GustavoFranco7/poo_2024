#Manejo de errores es la froma que tienen los lenguajes de programacion 
#para evitar que sucedan errores en tiempo de ejecucion

#Ejemplo 1: Error cuando una variable no se genera

# try:
#     nombre=input("Dame el nombre ")

#     if len(nombre)>1:
#         nombre_usuario="El nombre es: "+nombre
#     print(nombre_usuario)
# except:
#     print("Es necesario introducir un nombre de usuario")

#Ejemplo 2: Cuando se solicita un numero y se introduce una letra

# try:
#  numero=int(input("Dame un numero "))
#  if numero>0:
#     print("soy un numero entero positivo ")
#  else:
#     print("soy un numero entero negativo")
# except:
#     print("No se puede convertir un caracter no numerico ")
# else:
#     print("Todo se ejecuto sin errores")

#Ejemplo 3: Cuando se generan multiples excepciones

try:
 numero=int(input("Dame un numero "))
 print("el cuadrado es:"+ str(numero*numero))
except ValueError:
    print("debes introduucir un numero")
except TypeError:
    print("debes introduucir un numero")
else:
    print("finalizo correctamente")
finally:
    print("termine")


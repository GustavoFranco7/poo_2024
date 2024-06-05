"""
una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa
sintaxis:

def NombreDeMiFuncion(Parametros):
bloque o conjunto de instrucciones

nombredemifuncion(parametros)

las funciones pueden ser de 4 tipos
1:-Funcion que no recibe parametros y no regresa valor
2:-Funcion que no recibe parametros y no regresa valor
"""

#Ejemplo 1:-Funcion que no recibe parametros y no regresa valor
"""
def sumaNumeros1():
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")
    
    sumaNumeros1()
"""
"""
#Ejemplo 2.-Funcion que no recibe parametros y regresa valor
def sumaNumeros2():
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    suma=n1+n2
    return f"{n1}+{n2}={suma}"

cadena=sumaNumeros2()
print(cadena)
"""
#Ejemplo 3.-Funcion que recibe parametros y no regresa valoe
"""
def sumaNumeros3(n1,n2):
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")
n1=int(input("Numero #1:"))
n2=int(input("Numero #2:"))
sumaNumeros3(n1,n2)
"""
#Ejemplo 4.-Funcion que recibe parametros y regresa valoe

def sumaNumeros4(n1,n2):
    suma=n1+n2
    return f"{n1}+{n2}={suma}"
n1=int(input("Numero #1:"))
n2=int(input("Numero #2:"))
print(sumaNumeros4(n1,n2))

#Eejmplo: crear un programa que solicite a traves de una funcion la siguiente informacion:
#Nombre del paciente, edad, estatura, tipo de sangre, utilizar las 4 tipos de funciones



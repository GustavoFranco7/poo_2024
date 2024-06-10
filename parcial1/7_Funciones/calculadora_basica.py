"""
print("\nCalculadora basica\n 1-suma\n 2-resta \n 3-multiplicacion\n 4-division \n 5-Salir")
opcion= input("\tElige una opcion").upper()
"""
"""
if opcion=="1" or opcion =="+" or opcion =="SUMA":   
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")
elif opcion=="2" or opcion =="-" or opcion =="RESTA": 
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    resta=n1-n2
    print(f"{n1}-{n2}={resta}")
elif opcion=="3" or opcion =="*" or opcion =="MULTIPLICAR": 
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    multi=n1*n2
    print(f"{n1}*{n2}={multi}")
elif opcion=="4" or opcion =="/" or opcion =="DIVIDIR": 
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    divi=n1/n2
    print(f"{n1}/{n2}={divi}")
else: 
    print ("Gracias por utilizar el sistema")
"""
"""
if int(opcion)>=1 and int(opcion)<=4 or opcion=="1" or opcion =="+" or opcion =="SUMA" or "3" or opcion =="*" or opcion =="MULTIPLICAR" or "4" or opcion =="/" or opcion =="DIVIDIR":
    n2=int(input("Numero #2:"))

if opcion=="1" or opcion =="+" or opcion =="SUMA":   
    print(f"{n1}+{n2}={n1+n2}")
elif opcion=="2" or opcion =="-" or opcion =="RESTA": 
    print(f"{n1}-{n2}={n1-n2}")
elif opcion=="3" or opcion =="*" or opcion =="MULTIPLICAR": 
    print(f"{n1}*{n2}={n1*n2}")
elif opcion=="4" or opcion =="/" or opcion =="DIVIDIR": 
    print(f"{n1}/{n2}={n1/n2}")
else: 
    print ("Gracias por utilizar el sistema")
"""
import os

from Varias_funciones import *
# import Varias_funciones

#def solicitarNumeros():
    #global n1,n2
    #n1=int(input("Numero # 1:"))
    #n2=int(input("Numero # 2:"))


#def calculadora(n1,n2,opcion):
    #if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
   #     return f"{n1}+{n2}={n1+n2}"
    #elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
    #    return f"{n1}-{n2}={n1-n2}"
   # elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
    #    return f"{n1}*{n2}={n1*n2}"
    #elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
      #  return f"{n1}/{n2}={n1/n2}"
    #else:
       # opcion=False
       # return "Gracias por utilizar el sistema ..."

#def esperetecla():
  #  print("Oprima una tecla para continuar")
 #   input()
           

opcion=True
while opcion:
    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    if opcion !="5":
     n1,n2=solicitarNumeros()
     print(calculadora(n1,n2,opcion))
     esperetecla()
    else:
        opcion=False
        print ("Gracias por utilizar el sistema ...")
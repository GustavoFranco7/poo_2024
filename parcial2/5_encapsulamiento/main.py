
from coches import *

#Crear un objetos o instanciar la clase
print("Objeto 1")
coche1=Coches("Blanco", "VW", "2022", 220, 150, 5)


# coche1.getInfo()



# print("Objeto 2")
# coche2=Coches("Azul", "Nissan", "2020", 100, 150, 6)

# coche2.getInfo()

#Implementar el encapsulamiento o visibilidad
print(coche1.atributo_publico)
#print(coche1.__atributo_privado) #no es posible
print(coche1.MetodoPublico())
#coche1.__MetodoPrivado()#no es posible
coche1.getMetodoPublico()

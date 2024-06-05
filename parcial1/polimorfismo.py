#Definir clase base Animal

class Animal:
    def hacer_soido(self):
        pass

#Definir subclases
class perro:
    def hacer_soido(self):
        return "Guau"

class gato:
    def hacer_soido(self):
        return "Miau"

class vaca:
    def hacer_soido(self):
        return "Muuu"

animales= [perro(), gato(), vaca()]

for animal in animales:
    print(animal.hacer_soido())


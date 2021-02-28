# -*- coding: utf8 -*-
import json
import time


class CoffeeMachine:
    WATER_LEVEL = 100

# Une méthode protégée est accessible à l'intérieur d'une classe mais ne doit pas être
# aisément accessible de l'extérieur. Vous ajoutez pour cela "un underscore" au début du nom de la méthode
    def _start_machine(self):
        if self.WATER_LEVEL > 20:
            return True
        else:
            print("Please, add water !")
            return False

# Une "méthode privée" est accessible à l'intérieur d'une classe mais ne doit absolument
# pas être accessible de l'extérieur. Vous ajoutez pour cela "deux underscores" au début du nom de la méthode
    def __boil_water(self):
        return "boiling..."

    def make_coffee(self):
        if self._start_machine():
            self.WATER_LEVEL -= 20
            print(self.__boil_water())
            print("Coffee is ready !")

cafetiere = CoffeeMachine()
cafetiere.make_coffee()
print("")
for i in range(4):
    cafetiere.make_coffee()
    print("")


print("Make Coffee: Public", cafetiere.make_coffee())       # Méthode Publique : on peut l'appeler de l'extérieur de la class "CoffeeMachine"
print("Start Machine: Protected", cafetiere._start_machine())   # Méthode Potégée : il faut ajouter "un underscore" pour l'appeler de l'extérieur
print("Boil Water: Private", cafetiere.__boil_water())      # Méthode Privée : même en rajoutant "2 underscores" on ne peut l'appeler de l'extérieur
print("Boil Water: Private", cafetiere._CoffeeMachine__boil_water())  # en fait, on peut tout de même l'appeler en ajoutant le nom de la class devant


# -*- coding: utf8 -*-
import re
import time

print()

# Le but de ce code est de montrer l'utilité de l'instruction "dir()
# qui renvoie tous les attributs et méthodes utilisés par un objet (y compris les "méthodes spéciales")

class Porte_monnaie:

    def __init__(self, monnaie_val):
        self.monnaie = monnaie_val

    def ajouter_monnaie(self, monnaie_val):
        self.monnaie = self.monnaie + monnaie_val
    
    def afficher_monnaie(self):
        print("Le porte-monnaie contient ", self.monnaie, " €")
    
def main():
    porte_monney = Porte_monnaie(10)
    porte_monney.ajouter_monnaie(20)
    porte_monney.ajouter_monnaie(35)
    porte_monney.afficher_monnaie()
    print(dir(porte_monney))            # l'instruction "dir()" renvoie tous les attributs et méthodes utilisés par l'objet "a"  =>
                                        # résultat = ['afficher_monnaie', 'ajouter_monnaie', 'monnaie'] (hors methodes spéciales)

    print()
    Director = []
    for element in dir(Porte_monnaie):  # même fonction que "dir()" mais renvoie uniquement les méthodes non spéciales 
        if str(element)[0:2] != "__":
            Director.append(str(element))
    print(Director)

main()


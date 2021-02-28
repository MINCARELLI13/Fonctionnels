# -*- coding: utf8 -*-
import json
import time

# Le but de ce code est de montrer l'utilité de l'instruction "dir()
# qui renvoie tous les attributs et méthodes utilisés par un obejt (y compris les "méthodes spéciales")

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
    print(dir(porte_monney))            # l'instruction "dir()" renvoie tous les attributs et méthodes utilisés par l'obejt "a"  =>
                                        # résultat = ['afficher_monnaie', 'ajouter_monnaie', 'monnaie'] (hors methodes spéciales)


main()


#!/usr/bin/env python

print()

class Compteur:
    """ Cette classe possède un attribut de classe qui s'incrémente à chaque fois que l'on crée un objet de ce type """
    objets_crees = 0 # Le compteur vaut 0 au départ

    def __init__(self):
        """ A chaque fois qu'on crée un objet, on incrémente le compteur """
        Compteur.objets_crees += 1

    def combien(cls):       # ! Attention : on utilise "cls" et non plus "self" !
        """ Méthode de classe affichant combien d'objets ont été créés """
        print("Jusqu'à présent, {} objets ont été créés.".format(cls.objets_crees))

    combien = classmethod(combien)      # !!! Tout se joue ici !!!

Compteur.combien()      # Jusqu'à présent, 0 objets ont été créés.

a = Compteur()
Compteur.combien()      # Jusqu'à présent, 1 objets ont été créés.

b = Compteur()
Compteur.combien()      # Jusqu'à présent, 2 objets ont été créés.




# -*- coding: utf8 -*-
import json

class Chiffres:                 # création des chiffres avec comme attribut leur valeur ("1" par exemple) 

    DICO_CHIFFRES_LETTRES = {1:"un", 2:"deux", 3:"trois", 4:"quatre", 5:"cinq", 6:"six", 7:"sept", 8:"huit",9:"neuf", 0:"zero"}

    DICO_FR_EN = {"un":"one", "deux":"two", "trois":"three", "quatre":"four", "cinq":"five", "six":"six", "sept":"seven", "huit":"height","neuf":"nine","zéro":"zero"}

    def __init__(self, chiffre_val):            # initialisation de l'objet "chiffre_x"
        self.chiffre = chiffre_val              # l'attribut "chiffre" prend la valeur "chiffre_val"
    
    @property                           # ici, on transforme la fonction "chiffre_lettres" en attribut de l'objet
    def chiffre_lettres(self):                  # construction d'une fonction qui transforme un chiffre en lettres
            return self.DICO_CHIFFRES_LETTRES[self.chiffre]
    
    @property                           # ici, on transforme la fonction "chiffre_en" en attribut de l'objet
    def chiffre_eng(self):                      # fonction qui transforme un chiffre (en lettres) en sa traduction anglaise
        return self.DICO_FR_EN[self.chiffre_lettres]




def main():
    chiffre_un = Chiffres(1)
    print(chiffre_un.chiffre, " / ", chiffre_un.chiffre_lettres, " / ", chiffre_un.chiffre_eng)
    chiffre_cinq = Chiffres(5)
    print(chiffre_cinq.chiffre, " / ", chiffre_cinq.chiffre_lettres, " / ", chiffre_cinq.chiffre_eng)


main()
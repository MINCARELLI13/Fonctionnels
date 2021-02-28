# -*- coding: utf8 -*-

# Le but de ce code est de donner un exemple d'utilisation d'une "méthode de classe" (à la différence d'une méthode d'instance)

class Porte_monnaie:
    # Cette classe possède un "attribut de classe" qui s'incrémente à chaque fois que l'on crée un objet de ce type

    OBJETS_CREES = 0        # Le compteur vaut 0 au départ
    
    def __init__(self, monnaie_val):
        # on crée un objet porte_monnaie avec une certaine somme
        self.monnaie = monnaie_val
        # À chaque fois qu'on crée un objet, on incrémente le compteur
        Porte_monnaie.OBJETS_CREES += 1
    
    @classmethod
    def combien(cls):
        # Méthode de classe affichant combien d'objets ont été créés
        print("Jusqu'à présent, {} objets ont été créés.".format(cls.OBJETS_CREES))
    # combien = classmethod(combien)   est une autre façon de déclarer une "méthode de classe"


print("")
Porte_monnaie.combien()     # on affiche le nombre d'objets créés avant même d'en avoir créés un grâce à la "@classmethod" combien()
                            # qui ne nécessite pas d'avoir créée un objet précédemment pour pouvoir appeler cette méthode à partir de lui
print("")

a = Porte_monnaie(10)
print("Le premier porte_monnaie contient ", a.monnaie, " €", end=" .....    ")
Porte_monnaie.combien()
print("")

b = Porte_monnaie(20)
print("Le second porte_monnaie contient ", b.monnaie, " €", end=" .....    ")
Porte_monnaie.combien()
print("")

# print("Salut !")

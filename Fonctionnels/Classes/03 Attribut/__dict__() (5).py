# -*- coding: utf8 -*-

# Le but de ce code est d'utiliser la méthode spéciale "__dict__" qui permet d'afficher tous les attributs d'un objet

class Utilisateur:

    def __init__(self, attrib_valeurs):
        for i in range(len(attrib_valeurs)):            # on parcours "my_list" = ["un", "deux", "trois"]
            nom = "attrib" + str(i)                     # on crée le nom d'un attribut : "attrib" suivi du numéro actuel de my_list
            setattr(self, nom, attrib_valeurs[i])       # on affecte chacune des 3 valeurs de la liste "attrib_valeurs"
                                                        # aux noms "fabriqués" : "attrib0", "attrib1" et "attrib2"

def main():
    my_list = ["un", "deux", "trois"]
    client = Utilisateur(my_list)       # on crée un objet "client" avec 3 attibutes passés sous forme de liste "my_list" = ["un", "deux", "trois"]
    print(client.__dict__)      # on affiche l'ensemble des attributs de l'objet "client" --> {'attrib0': 'un', 'attrib1': 'deux', 'attrib2': 'trois'}


main()
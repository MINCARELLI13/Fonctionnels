# -*- coding: utf8 -*-

# création d'une classe "minimale" avec 2 attributs (...)
# et une méthode "set_nom" qui permet de créer l'attribut "nom" pour un objet "Utilisateur()"
class Utilisateur:

    statut = "inscrit"              # création "minimale" d'un attribut "statut" initialisé à "inscrit"
    age = 0                         # création "minimale" d'un attribut "age" initialisé à "0"
    
    def set_nom(self, le_nom):      # création "minimale" d'une méthode "set_nom" qui permet de créer l'attribut "nom"
        self.nom = le_nom               # # création de l'attribut "nom" qui prend la valeur "le_nom"

personne_une = Utilisateur()        # création de l'objet "personne_une" par instanciation de la classe "Utilisateur"
personne_deux = Utilisateur()       # création de l'objet "personne_deux" par instanciation de la classe "Utilisateur"

personne_une.age = 30               # modification de la valeur de l'attribut "age" de l'objet "personne_une"
print(personne_une.age)             # l'attribut "age" de l'objet "personne_une" affiche maintenant "30" au lieu de "0"
print(personne_deux.age)            # l'attribut "age" de l'objet "personne_deux" affiche toujours "0"
print(type(personne_une.age))       # l'attribut "age" de l'objet "personne_une" est de type 'int' (car il a pour valeur "30")

personne_une.set_nom("Pierre")      # création de l'attribut "nom" avec la méthode "set_nom" pour l'objet "personne_une"
print(personne_une.nom)             # l'objet "personne_une" possède un nouvel attribut "nom" qui a pour valeur "Pierre"

personne_deux.sexe = "femme"        # création ex nihilo d'un nouvel attribut "sexe" sans utilisation d'une méthode de "Utilisateur()"
print(personne_deux.sexe)           # l'attribut "sexe" de l'objet "personne_deux" affiche "femme"


print(personne_deux.nom)            # l'objet "personne_deux" ne possède pas d'attribut "nom" alors qu'elle est issue de la même
                                    # classe que l'objet "personne_une" (AttributeError: 'Utilisateur' object has no attribute 'nom')




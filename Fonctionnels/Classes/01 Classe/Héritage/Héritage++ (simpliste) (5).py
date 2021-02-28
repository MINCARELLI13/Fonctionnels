# -*- coding: utf8 -*-
import json
import time

# https://www.pierre-giraud.com/python-apprendre-programmer-cours/oriente-objet-heritage-polymorphisme/

# création de la classe de base (ou classe parent)
class Utilisateur:

    def __init__(self, name_val, age_val):
        self.user_name = name_val
        self.user_age = age_val
    
    def getNom(self):
        print("Salut, je suis ", self.user_name)


# création de la sous-classe (ou classe enfant) qui prend "entre parenthèses" pour argument la classe de base "Utilisateur"
class Client(Utilisateur):
    is_client = True        # cette classe "Client()" est totalement vide hormis cette ligne !
    # -------------------------------------------------------------------------------------------------------------------------------------
    # Si on ne met rien,par défaut, la sous classe "Client()" aura la même initialisation
    # "__init__(self, name_val, age_val)" que la classe de base "Utilisateur()";
    # il y a HERITAGE de tous les attributs et méthodes de la classe "Utilisateur()"  ! ! !
    # -------------------------------------------------------------------------------------------------------------------------------------




# utilisation de l'héritage de classe...
utilisatrice = Utilisateur("Mathide", 28)   # on crée l'objet "utilisatrice"
client_one = Client("Pierre", 29)           # on crée aussi l'objet "client_one" à partir de la classe "Client()"
                                            # mais avec les paramètres "nom" et "âge" hérités de la classe "Utilisateurs()"  ! ! !

utilisatrice.getNom()           # on utilise, normalement, la méthode "getNom()" de la classe "Utilisateur()"
client_one.getNom()             # on utilise, anormalement, la méthode "getNom()" non définie dans la classe "Client()"

print("Age de client_one : ", client_one.user_age)  # ici, un objet de la classe "Client()" utilise un attribut de la classe "Utilisateur()"
print(client_one.is_client)     # on utilise, normalement, un attribut de la classe "Client()" qui n'existe pas dans la classe "Utilisateur()"
print(utilisatrice.is_client)   # en revanche, on ne peut pas utiliser un attribut d'une "sous classe" pour un objet de la "classe de base"


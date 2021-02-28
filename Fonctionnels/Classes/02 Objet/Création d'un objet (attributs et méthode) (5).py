# -*- coding: utf8 -*-

class Utilisateur:                      # création de la classe "Utilisateur"

    def __init__(self, prenom, age):    # initialisation de la classe avec création des attributs
        self.user_name = prenom         # création de l'attribut "user_name" qui contiendra le prénom du client (ie de l'utilisateur)
        self.user_age = age             # création de l'attribut "user_age" qui contiendra l'âge du client (ie de l'utilisateur)
    
    def affich_nom_age(self):           # # création de la méthode "affich_nom_age" qui affichera le prénom et l'âge du client
        print(f"Je m'appelle {self.user_name} et j'ai {self.user_age} ans.")

first_client = Utilisateur("Pierre", 29)        # création d'une instance "Utilisateur" (un objet) appelé "first_client"
first_client.affich_nom_age()                   # utilisation de la méthode "affich_nom_age" qui permet d'afficher Prénom et age du client

second_client = Utilisateur("Sophie", 50)        # création d'un objet, de la classe "Utilisateur", appelé "second_client"
second_client.affich_nom_age()                   # utilisation de la méthode "affich_nom_age" qui permet d'afficher Prénom et age du client

print(first_client.__dict__)
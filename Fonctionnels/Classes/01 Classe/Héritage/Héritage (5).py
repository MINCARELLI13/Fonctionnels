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

    def __init__(self, name_val, age_val, email_val):       # on initialise les objets, à l'identique, de la classe "Utilisateur()" + "email_val"
        Utilisateur.__init__(self, name_val, age_val)       # on récupère, à l'identique, tous les attributs de la classe de base "Utilisateur()"
        self.user_email = email_val                     # et on "SURCHARGE" la méthode __init__() de "Utilisateur()" avec l'attribut "email" ! ! !

    # Python va utiliser cette méthode "getNom()" propre à la classe "Client()" en priorité...
    # ... et si elle n'existait pas, il irait utiliser la méthode "getNom()" héritée de la classe "Utilisateur()"
    def getNom(self):
        print("Salut, je suis ", self.user_name, " et mon mail est :", self.user_email)

utilisateur_one = Utilisateur("Mathide", 28)   # on crée l'objet "utilisatrice"
client_one = Client("Pierre", 29, "toto@laposte.net")   # on crée aussi l'objet "client_one" avec les attributs "nom" et "âge" hérités
                                                        # de la classe "Utilisateurs()" mais SURCHARGE de l'attribut "email"   ! ! !

print("")

print(utilisateur_one.user_name)       # l'objet "utilisateur_one" a été instancié à partir de la classe de base "Utilisateur()"
print(client_one.user_name)       # l'objet "client_one" a été instancié à partir de la sous-classe "Client()" qui a hérité de la classe "Utilisateur()"

utilisateur_one.getNom()        # l'objet "utilisateur_one" utilise la méthode "getNom()" propre à la classe de base "Utilisateur()"
client_one.getNom()        # l'objet "client_one" utilise la méthode "getNom()" propre à la classe de base "Client()"

print(client_one.user_email)    # l'attribut "user.mail" est propre à la sous-classe "Client()"
print(utilisateur_one.user_email)    # l'attribut "user.mail" n'existe pas dans la classe de base "Utilisateur()" --> "ERROR ! ! !"


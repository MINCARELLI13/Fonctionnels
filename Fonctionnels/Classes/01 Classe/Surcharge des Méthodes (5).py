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

    # Python va utiliser cette méthode "getNom()" - propre à la classe "Client()" - en priorité...
    # ... et si elle n'existait pas, il irait utiliser la méthode "getNom()" héritée de la classe "Utilisateur()"
    def getNom(self):
        print("Salut, je suis ", self.user_name, " et mon mail est :", self.user_email)



# utilisation des de la surcharge des méthodes...
utilisatrice = Utilisateur("Mathide", 28)   # on crée l'objet "utilisatrice"
client_one = Client("Pierre", 29, "toto@laposte.net")   # on crée aussi l'objet "client_one" avec les attributs "nom" et "âge" hérités
                                                        # de la classe "Utilisateurs()" mais SURCHARGE de l'attribut "email"   ! ! !

utilisatrice.getNom()           # on utilise, la méthode "getNom()" de la classe "Utilisateur()"
client_one.getNom()             # ! ! !  on utilise, la méthode "getNom()" de la classe "Client()"   = SURCHARGE de la méthode  ! ! !

print("Age de client_one : ", client_one.user_age)  # ici, un objet de la classe "Client()" utilise un attribut de la classe "Utilisateur()"
print(client_one.user_email)     # on utilise, normalement, un attribut de la classe "Client()" qui n'existe pas dans la classe "Utilisateur()"

print(utilisatrice.user_email)   # en revanche, on ne peut pas utiliser un attribut d'une "sous classe" dans un objet de la "classe de base"


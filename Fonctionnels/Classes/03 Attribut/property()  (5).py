# -*- coding: utf8 -*-

print()

# le but de ce script est de montrer l'utilité du constructeur "property()"
# qui permet de "maitriser" les manipulations extérieurs sur les membres d'une classe (attributs et méthodes)

# Classe définissant une personne caractérisée par :  son nom ; son prénom ; son âge ; son lieu de résidence
class Personne:
    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris"  # Notez le souligné _ devant le nom

    # Méthode qui sera appelée quand on souhaitera accéder en lecture à l'attribut 'lieu_residence'
    def _get_lieu_residence(self):      
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence

    # Méthode appelée quand on souhaite modifier le lieu de résidence
    def _set_lieu_residence(self, nouvelle_residence):
        print("Attention, il semble que {} déménage à {}.".format(self.prenom, nouvelle_residence))
        if nouvelle_residence == "Nice 06" or nouvelle_residence == "Digne 04":
            self._lieu_residence = "le sud"
        else:
            self._lieu_residence = nouvelle_residence

    # On va dire à Python que notre attribut lieu_residence pointe vers une propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)     # !!! tout se joue ici !!!


# ------------------- main
le_mec = Personne("Tholo", "Sergio")
print()
print(le_mec.prenom, le_mec.nom, "est le meilleur")
le_mec.age = 57
le_mec.lieu_residence = "Digne 04"          # !!! ici, le "lieu_residence" modifié n'est pas celui qui s'affiche !!!
print(le_mec.prenom, le_mec.nom, " est agé de", le_mec.age,"ans et il habite", le_mec.lieu_residence, "pour toujours")

# !!! au final, il apparaît impossible pour un utilisateur extérieur de changer l'adresse de Sergio
# pour "Digne 04" ou "Nice 06"; en revanche, ça fonctionne pour toute autre nouvelle adresse !!!

#           !           
#           !
#           !
#           !   
#           v

#   UN AUTRE EXEMPLE DE "PROPERTY()"



# class Employe(object):
#     """Classe des Employés"""           # Documentation de la classe
#     def __init__(self, nom):
#         print("La classe à été initialisée...")
#         self.__nom = nom
 
#     def get_nom(self):                # Méthode 'get' pour retourner le nom
#         return self.__nom
 
#     def set_nom(self, nouveau_nom):   # Méthode 'set' pour modifier le nom
#         if nouveau_nom == "":
#             print("Le nom de l'employé ne peut pas être vide.")
#         else:
#             self.__nom = nouveau_nom
#             print("Le Nom à été modifié.")
 
#     nom = property(get_nom, set_nom)
 
#     def afficher(self):
#         print(self.nom, " a été ajouté")
 
# # main
# obj = Employe("Jim kamson")  # Initialiser un objet de la classe
# obj.afficher()               # Accéder à une méthode de la classe
 
# print("Nom de l'employé est:", obj.nom)        # Accéder à une propriété de la classe
# print("Modification du nom de la classe.")
# obj.nom = ""                # Génération d'une erreur, Nom est vide
 
# obj.nom = "Raul"
# obj.afficher()
    
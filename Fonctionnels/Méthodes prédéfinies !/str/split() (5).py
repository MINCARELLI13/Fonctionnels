# -*- coding: utf8 -*-
#!/usr/bin/python

# # La méthode "split()" permet de découper une chaîne de caractères en "mots" séparés par un séparateur (espace, virgule...)
print("-------------------------------------------------------------")

animaux = "girafe, tigre, singe, souris"    # un chaine de caractère constituée de 4 animaux séparés par des virgules
animaux_liste = animaux.split(",")          # attention, ici le séparateur est la virgule ","

for animal in animaux_liste:
    print(animal, end=" ")
print("")


# # Autre script classique utilisant "split()" : on demande d'entrer deux nombres que l'on récupère dans les variables numerateur et denominateur
print("-------------------------------------------------------------")

# on récupère dans la liste "donnees" les deux nombres entrés par l'utilisateur
donnees = ((input("Entrez deux nombres positifs : (exple, 72.19  35.28)  ")).strip()).split()   # "strip()" ote les espaces devant et derrière les nb
print(donnees)                      # les deux nombres sont alors enregistrés dans le tableau "donnees"
numerateur, denominateur = donnees [0], donnees[1]      # on transfère les deux valeurs dans les variables "numerateur" et "denominateur"
print("numérateur = ", numerateur)
print("dénominateur = ", denominateur)
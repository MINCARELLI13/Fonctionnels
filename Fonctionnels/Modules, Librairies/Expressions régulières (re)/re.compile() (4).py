#!/usr/bin/env python
# Ajoute des guillemets à tous les mots suivent "livre"
import re
print()

# On veut vérifier que le mot de passe attendu fait bien six caractères au minimum
# et qu'il ne contient que des lettres majuscules, minuscules et des chiffres
chaine_attendue = r"^[A-Za-z0-9]{6,}$"

chaine_mdp = re.compile(chaine_attendue)    # on enregistre la chaine attendue dans chaine_mdp !!!

mot_de_passe = ""
while chaine_mdp.search(mot_de_passe) is None:          # et on recherche cette chaine_mdp dans la chaine mot_de_passe fourni par l'utilisateur
    mot_de_passe = input("Tapez votre mot de passe : ")

print("mot de passe valide !")

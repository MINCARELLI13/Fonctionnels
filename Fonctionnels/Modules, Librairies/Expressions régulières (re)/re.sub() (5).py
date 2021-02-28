#!/usr/bin/env python
# Ajoute des guillemets à tous les mots suivent "livre"
import re
print()

texte = """nom='Task1', id=8, nom='Task2', id=31, nom='Task3', id=127"""
print("AVANT :", texte)
# on repère le "groupe" à remplacer par des parenthèses et on lui donne un nom "The_Cure" :)
print("APRES :",re.sub(r"(?P<The_Cure>Task)", r"Tâche", texte)) # remplace le mot "Task" par "Tâche"
print("APRES :",re.sub(r"(?P<The_Cure>=)", r" = ", texte))      # remplace "=" par " = "



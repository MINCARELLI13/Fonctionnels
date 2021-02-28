#!/usr/bin/env python
# Ajoute des guillemets à tous les mots suivent "livre"
import re
print()

regex = re.compile(r"([0-9]+).([0-9]+)")
resultat = regex.search("pi vaut 3.14")

pi = resultat.group(0)
partie_entiere = resultat.group(1)
partie_decimale = resultat.group(2)

print(pi, "est composé d'une partie entière", '"' + partie_entiere, '"' + "et d'une partie décimale" + '"', partie_decimale +'"')


# # Le but est de mettre des "guillemets" autour du second mot "Python" de la phrase "chaine" (et pas du premier "Python")
# # C'est pour cette raison que la recherche se fait par la position du groupe "\1" qui caractérise le mot "Python" recherché
# # ce groupe "\1" (= "(\w+)") est une chaîne de caractères qui a pour caractéristique d'être situé juste après le mot "livre" : r'livre (\w+)'
# chaine = "Test regex Python pour le livre Python de Wikibooks francophone."
# chaineTriee = re.sub(
#                   r'livre (\w+)',   # ensemble des lettres et nombres (ici, "Pyhton") situé après la chaîne "livre", et qui s'arrête avec l'espace d'après
#                       r'livre "\1"',
#                           chaine)
# print("AVANT : ", chaine)
# print("APRES : ", chaineTriee)       # Affiche "Test regex Python pour le livre "Python" de Wikibooks francophone."


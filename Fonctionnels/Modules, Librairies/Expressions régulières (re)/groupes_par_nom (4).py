#!/usr/bin/env python
# Ajoute des guillemets à tous les mots suivent "livre"
import re
print()

# correspond à la recherche d'un nombre décimal (25.54 ou 0.91 ou 7.659 ...)
regex = re.compile(r"([0-9]+).([0-9]+)")    # on remarquera ici les 3 groupes : (l'ensemble du décimal), le premier "([0-9]+)" et le second "([0-9]+)"
resultat = regex.search("le nombre pi vaut 3.14")     # on recherche un nombre décimal dans la chaîne "le nombre pi vaut 3.14"

pi = resultat.group(0)              # ici, on récupère le résultat en entier : group(0) = "3.14"
partie_entiere = resultat.group(1)  # ici, on récupère la première partie du résultat : group(1) = "3"
partie_decimale = resultat.group(2) # ici, on récupère la seconde partie du résultat : group(2) = "14"

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

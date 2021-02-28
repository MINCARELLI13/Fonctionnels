#!/usr/bin/env python

print()

# Le but de ce script est de montrer comment lire un fichier ".txt"

fich_var = open("essai_fichier.txt")     # on ouvre le fichier nommé "essai_fichier.txt" et on lui affecte la variable "fich_var" pour le manipuler
try:
    for ligne in fich_var.readlines():   # !!! on lit tout le contenu de "fich_var" ligne après ligne avec la méthode "readlines()" !!!
        print(ligne, end="")
finally:
    fich_var.close()                     # on ferme le fichier "fich_var"
print()



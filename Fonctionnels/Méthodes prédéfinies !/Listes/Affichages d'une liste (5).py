# -*- coding: utf8 -*-
import random
import json

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(x[3])			        # Affiche la valeur du 4ème élément 

print(x[3:5])               # Affiche les nombres entre l'indice 3 inclus et 5 exclus

for i in range(0,8,2):		# Affiche les nombres entre l'indice 2 inclus et 8 exclus, par saut de 2 
	print(x[i])

print(len(x))               # Affiche la longueur de la liste x

print(min(x))               # Affiche la valeur minimum de x

print(max(x))               # Affiche la valeur maximale de x

print(sum(x))               # Affiche la somme des valeurs contenues dans la liste x


# -*- coding: utf8 -*-
import random


# la liste ci-dessous est la même liste ["a", "b" , "c", "d", "e", "f", "g", "h", "i", "j"] mais en désordre
liste = ["e", "h", "g", "i", "f", "d", "b", "j", "c", "a"]   
print(liste)

# le principe est de faire remonter l'élément max (ici la lettre "j") en fin de liste (= index 9)
# puis de faire remonter le deuxième élément max (ici la lettre "i") en index (max-1 = 8) de la liste
# et ainsi de suite...
def tri_bulles(my_liste):
    for i in range (len(my_liste)-1,0, -1):
        for j in range(i):
            if my_liste[j]>my_liste[j+1]:
                my_liste[j], my_liste[j+1] = my_liste[j+1], my_liste[j]     # on inverse les éléments de la liste situés aux index j et j+1
    return my_liste

liste = tri_bulles(liste)
print(liste)

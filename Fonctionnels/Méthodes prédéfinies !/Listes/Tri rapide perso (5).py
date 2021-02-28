# -*- coding: utf8 -*-
#!/usr/bin/python
import time
import random


# le but de la partition d'une liste "[4,1,3,2]" est de prendre aléatoirement une valeur "pivot" (= tjrs le dernier élément de la liste, ici "2")
# et de créer 2 nouvelles listes "l1" et "l2" qui contiendront respectivement :
# tous les éléments INFERIERURS à la valeur "pivot" --> on les mettra dans la nouvelle liste "l1" (ici [1])
# tous les éléments SUPERIEURS à la valeur "pivot" --> on les mettra dans la nouvelle liste "l2" (ici [4,3])
def partition(liste):

    l1 = []             # sous-liste "l1" des éléments INFERIEURS  à la valeur "pivot"
    l2 = []             # sous-liste "l2" des éléments superieurs  à la valeur "pivot"
    pivot = liste[len(liste)-1]         # on prend pour valeur pivot le dernier élément de la "liste"
                                        # par définition, "pivot" sera toujours supérieur à tous les éléments de la liste "l1"
                                        # et sera toujours inférieur à tous les éléments de la liste "l2" ! ! !

    # on partitionne la "liste" en deux listes "l1" et "l2" (avec toujours le "pivot" entre les 2 listes "l1" et "l2")
    if len(liste) > 1:                      # inutile de partitionner une liste à 1 élément
        for i in range(len(liste)-1):       # pour chacun des éléments de la "liste" (sauf le dernier qui est la valeur "pivot")

            if liste[i] <= pivot:           # si "pivot" supérieur à la valeur testée "liste[i]" alors on met cette dernière dans "l1"
                l1.append(liste[i])
                         
            else:                           # si "pivot" inférieur à la valeur testée "liste[i]" alors on met cette dernière dans "l2"
                l2.append(liste[i])

    # pour chacune des partitions "l1" et "l2" trouvées ci-dessus, on repartitionne chaque liste "l1" et "l2"
        if len(l1) == 0:                            # "l1" est vide signifie qu'il ne reste plus qu'à partitionner "l2"
            return [pivot] + partition(l2)          # on concatène "pivot" avec la nouvelle partition de "l2"

        elif len(l2) == 0:                          # "l2" est vide signifie qu'il ne reste plus qu'à partitionner "l1"
            return partition(l1) + [pivot]          # on concatène la nouvelle partition de "l1" avec "pivot"

        else:               # ni "l1" ni "l2" ne sont vides donc on partitionne les 2 listes de manières "récursive" ! ! ! 
            return partition(l1) + [pivot] + partition(l2)      # on concatène les partitions de "l1" et "l2" avec "pivot" au milieu

    else:                   # si la liste n'a qu'un élément, inutile de pratiquer une nouvelle partition
        return liste        # on a notre liste triée puisqu'il n'y a qu'un élément


liste = [i for i in range(1000000)]
random.shuffle(liste)

debut = time.time()

partition(liste)

fin = time.time()
intervalle = fin - debut
print("Temps de calcul pour le tri_perso : ", intervalle)

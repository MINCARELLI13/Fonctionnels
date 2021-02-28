# -*- coding: utf8 -*-
#!/usr/bin/python
import random
import time


# Meilleur algorithhme de tri ! ! !
def tri_rapide(L):
    """trirapide(L): tri rapide (quicksort) de la liste L"""
    def tri_rap(L, g, d):
        pivot = L[(g+d)//2]
        i = g
        j = d
        while True:
            while L[i]<pivot:
                i+=1
            while L[j]>pivot:
                j-=1
            if i>j:
                break
            if i<j:
                L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
        if g<j:
            tri_rap(L,g,j)
        if i<d:
            tri_rap(L,i,d)
 
    g=0
    d=len(L)-1
    tri_rap(L,g,d)


liste = [i for i in range(1000000)]     # on génére une liste croissante de nombres
random.shuffle(liste)               # on mélange tous les éléments de la liste
# print(liste)

debut = time.time()

tri_rapide(liste)
# print(liste)

fin = time.time()
intervalle = fin - debut
print("Temps de calcul pour le tri_rapide : ", intervalle)
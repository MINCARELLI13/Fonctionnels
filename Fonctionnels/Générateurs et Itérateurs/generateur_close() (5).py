#!/usr/bin/env python

print()

def generateur(debut, fin):

        count = debut
        while count < fin:
            yield count
            count += 1

intervalle = generateur(5, 20)  # on crée le générateur "intervalle"

for element in intervalle:
    print(element, end=" ")
    if element >= 17:
        intervalle.close()      # interruption de la boucle


# pour appeler les méthodes du générateur, on doit le stocker dans une variable "intervalle" avant la boucle.
# Si on avait écrit directement "for nombre in generateur(5, 20)", on n'aurait pas pu appeler la méthode "close()" du générateur.



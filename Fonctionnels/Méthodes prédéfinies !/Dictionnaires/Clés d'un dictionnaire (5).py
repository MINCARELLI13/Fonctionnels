# -*- coding: utf8 -*-

# retourne toutes les clés d'un dictionnaire sous forme de liste
def cles_dico(nom_dico):
    return list(nom_dico)

dico_en_fr = {"one":"un", "two":"deux", "three":"trois"}
print(cles_dico(dico_en_fr))

# Résultat = ['one', 'two', 'three']

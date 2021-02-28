# -*- coding: utf8 -*-

# retourne le contenu d'un dictionnaire sous forme d'une succession 'clé', 'valeur' (dans une liste)
def contenu_dico(nom_dico):
    my_list = []
    for (cle,valeur) in nom_dico.items():     # récupère chaque paire (clé, valeur) du dictionnaire
        my_list.append(cle)             # ajoute la clé dans une liste
        my_list.append(valeur)          # ajoute la valeur à la suite de la liste
    return my_list
 
 # retourne toutes les clés d'un dictionnaire sous forme d'une liste
def cles_dico(nom_dico):
    my_list = []
    for cle in nom_dico:     # récupère chaque clé du dictionnaire
        my_list.append(cle)         # ajoute la clé dans une liste
    return my_list


dico_en_fr = {"one":"un", "two":"deux", "three":"trois"}
print("")
print(contenu_dico(dico_en_fr))

print("")
print(cles_dico(dico_en_fr))



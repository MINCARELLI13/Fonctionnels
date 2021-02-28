# -*- coding: utf8 -*-
import random
import json

x = {"key1":"valeur1", "key2":"valeur2"}

# affiche la valeur de la clé "key"
print(x["key1"])    # --> valeur1

# ajoute la valeur "toto" correspondante à la clé "titi" 
x["titi"] = "toto"
print(x)    # --> {'key1': 'valeur1', 'key2': 'valeur2', 'titi': 'toto'}

# remplace la valeur de la clé "titi" par "tata" 
x["titi"] = "tata"
print(x)    # --> {'key1': 'valeur1', 'key2': 'valeur2', 'titi': 'tata'}

# supprime la clé "titi" et sa valeur correspondante 
del(x["titi"])
print(x)    # --> {'key1': 'valeur1', 'key2': 'valeur2'}

# fusionne deux dictionnaires
dico_en_fr_1 = {"one":"un", "two":"deux", "three":"trois"}
dico_en_fr_2 = {"two":"DEUX", "three":"TROIS"}
dico_en_fr_1.update(dico_en_fr_2)		# la valeur "deux" du dico1 est remplacée par "DEUX" du dico2
print(dico_en_fr_1)     # --> {'one': 'un', 'two': 'DEUX', 'three': 'TROIS'}

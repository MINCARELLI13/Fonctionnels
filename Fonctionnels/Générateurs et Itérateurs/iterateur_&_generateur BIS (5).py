#!/usr/bin/env python

print()

def mon_generateur():
    yield 1
    yield 2
    yield 3


print(mon_generateur)       # <function mon_generateur at 0x00E57778>
print(mon_generateur())     # <generator object mon_generateur at 0x0123C840>
print()

mon_iterateur = iter(mon_generateur())      # on crée un itérateur (permet d'identifier un itérateur et d'ajouter une fonction "next()")
print(mon_iterateur)                        # <generator object mon_generateur at 0x0123C840>
print()

# on parcourt le générateur en répétant la fonction "next()"
print("next(mon_iterateur) : ", next(mon_iterateur))        # affiche next(mon_iterateur) :  1
print("next(mon_iterateur) : ", next(mon_iterateur))        # next(mon_iterateur) :  2
print("next(mon_iterateur) : ", next(mon_iterateur))        # next(mon_iterateur) :  3
print()     # si on réitérait un nouveau "next(mon_iterateur)" on aurait le message : "StopIteration"

# la boucle "for... in" fait la même chose que précédemment
for nombre in mon_generateur(): # Attention on exécute la fonction
    print(nombre)






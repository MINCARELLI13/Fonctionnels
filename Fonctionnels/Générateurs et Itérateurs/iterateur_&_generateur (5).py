#!/usr/bin/env python

print()

# Le but de ce script est de montrer comment fabriquer un itérarteur
# grâce à un générateur
def mon_generateur(data):
    iterateur = iter(data)      # Python va vérifier en premier qu'il a bien affaire à un itérateur donc il nous faut le créer
    for index in range(len(data)):
        yield next(iterateur)       # ici, on prend l'élément suivant dans l'itérateur et on le renvoie avec le générateur "yield"

if __name__ == ('__main__'):
    generateur = mon_generateur("hello world")

    for value in generateur:
        print(value, end=" ")





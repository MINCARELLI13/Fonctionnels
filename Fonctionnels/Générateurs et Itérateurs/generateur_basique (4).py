#!/usr/bin/env python

print()

def mon_generateur():
    yield 'h'
    yield 'e'
    yield 'l'
    yield 'l'
    yield 'o'
    yield ' '
    yield 'w'
    yield 'o'
    yield 'r'
    yield 'l'
    yield 'd'

if __name__ == ('__main__'):
    generateur = mon_generateur()
    print("Objet généré : ", generateur)

    for value in generateur:
        print(value, end=" ")
    print()






#!/usr/bin/env python
print()

# Le but de ce script est de pouvoir générer des itérateurs perso ie avec des ensembles contenant des éléments ad hoc

# permet de générer un itérateur contenant un nombre "self.max" d'éléments
class MonIterateur:

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self, max_val):
        self.compteur = -1
        self.max = max_val
    
    # permet de définir comme itérateur l'objet créé avec la classe "MonIterateur"
    # Python va envoyer une demande pour savoir s'il peut itérer sur l'objet créé 
    def __iter__(self):
        # print(self)
        return self
    
    # Python va procéder à une succession de "__next__" et donc appeler systématiquement la méthode ci-dessous
    # jusqu'à ce que cette méthode lui renvoie un "raise StopIteration()"
    def __next__(self):
        self.compteur += 1
        if self.compteur>=self.max:
            raise StopIteration()    # sinon un simple "exit()" fonctionne très bien aussi à la place du "raise StopIteration"
        else:
            return self.alphabet[self.compteur]
             

# on construit un itérateur contenant les 5 premières lettres de l'alphabet : a, b, c, d, e
un_iterateur = MonIterateur

# la boucle "for... in" va effectuer 2 actions :
# la première est de vérifier que l'objet "un_iterateur" est effectivement un itérateur (c'est toute l'utilité de la méthode "__iter__()")
# la seconde est d'utiliser la méthode "__next__()" pour passer d'une valeur à la valeur suivante dans un ensemble (ici, la liste "alphabet")
for i in un_iterateur(26):
    print(i, end=" ")
print()
print("list(un_iterateur(26)) : ", list(un_iterateur(26)))   # 


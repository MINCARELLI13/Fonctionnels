#!/usr/bin/env python
print()

# Le but de ce script est de montrer qu'on peut créer des arrtibuts et des méthodes à l'extérieur d'une classe
# et ensuite s'en servir normalement dans des instances créées par la suite

def director(var):
    Director = []
    for element in dir(var):  # même fonction que "dir()" mais renvoie uniquement les méthodes et attributs non spéciaux
        if str(element)[0:2] != "__":
            Director.append(str(element))
    return Director

def funct(self):
    self.value += 1
    return self.value

# création d'une classe vide !
class Empty(object):
    pass

Empty.value = 0             # on crée l'attribut "value" pour la classe "Empty()" mais en dehors de ladite classe
Empty.fonction = funct      # on crée la méthode "fonction" pour la classe "Empty()" mais en dehors de ladite classe

empt = Empty()              # on crée une instance "empt" de la classe "Empty()"

print(empt.value)           # on utilise l'attribut "value" créé à l'extérieur de la classe comme s'il avait été créé à l'intérieur de la classe
print(empt.fonction())      # on utilise la méthode "fonction()" créé à l'extérieur de la classe comme si elle avait été créée à l'intérieur de la classe  
print(director(empt))       # on vérifie que l'instance créée a bien hérité de l'attribut et la méthode de la classe créés extérieurement



# iterable = [1, 2, 3, 4]
# print(iterable)
# iterator = iter(iterable)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# print()

# class MonIterateur:

#     max_val = 5

#     def __init__(self): # , max_val):
#         self.max = self.max_val
#         self.compteur = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.compteur += 1
#         if self.compteur <= self.max:
#             return self.compteur
#         else:
#             raise StopIteration

# iterateur_un = MonIterateur()

# for i in iterateur_un:
#     print(i, iterateur_un.__iter__)

# print()
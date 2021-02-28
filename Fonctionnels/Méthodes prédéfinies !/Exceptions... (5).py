#!/usr/bin/env python

print()


annee = input() # L'utilisateur saisit l'année
try:
    annee = int(annee) # On tente de convertir l'année
    if annee<=0:
        raise NameError ("l'année saisie est négative ou nulle")    # on lève volontairement une exception si annee<=0 !!!
except ValueError:                          # cette exception est générée automatiquement par Python si on ne fournit pas un entier
    print("La valeur saisie est invalide.")
except NameError:                                                   # ici, on traite l'execption "NameError" levée avec le "raise" !!!
    print("Erreur de saisie : l'année est peut-être négative ou nulle")




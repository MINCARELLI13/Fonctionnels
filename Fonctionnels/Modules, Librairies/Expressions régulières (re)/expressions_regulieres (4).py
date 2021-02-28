import re

print("")

# Notre regex doit vérifier qu'une chaîne est un numéro de téléphone à 10 chiffres
# Les différentes formes valables attendues sont : "0x xx xx xx xx" ou "0x-xx-xx-xx-xx" ou "0xxxxxxxxx" ou "0x.xx.xx.xx.xx." (avec 1 point à la fin)

chaine = " 04 9236-65.41. "

expression = "^[ ]{0,5}?0[0-9]([ .-]?[0-9]{2}){4}[ .]{0,5}?$"
# "^[ ]{0,5}?"  -->  accepte jusqu'à 5 espaces devant le numéro de téléphone (espace = [ ] et "5 fois" = {0,5})
# "0[0-9]"  -->  attend un "0" comme premier chiffre suivi d'un autre chiffre compris entre "0" et "9"
# "([ .-]?[0-9]{2}){4}"  -->  attend {soit 1 espace, soit 1 point, soit 1 tiret, soit rien} suivi de 2 chiffres successifs (entre 0 et 9) "4 fois"
# "[ .]{0,5}?"  -->  accepte jusqu'à {soit 5 espaces, soit 5 points, soit rien du tout} derrière le numéro de téléphone

while re.search(expression, chaine) is None:
    chaine = input("Saisissez un numéro de téléphone (valide) :")

if re.search(expression, chaine):
    print("Bravo ! (", chaine, ")")


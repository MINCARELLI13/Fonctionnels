# -*- coding: utf8 -*-
#!/usr/bin/python


# Ce script permet de gérer différentes erreurs dans l'affectation de nombres dans 2 variables
# et dans le calcul d'une division
print("---------------------------------------------------------------------------------------")


# un utilisateur propose deux nombres positifs que l'on récupère dans les variables numerateur et denominateur
# le but est de gérer les 3 erreurs suivantes :
#   1) si l'utilisateur a oublié de rentrer une des 2 valeurs (IndexError)
#   2) si l'utilisateur a rentré "0" comme seconde valeur (ValueError car division par "0")
#   3) si l'utilisateur a rentré autre chose qu'un nombre (ValueError car impossibilité de "floater" les valeurs proposées)
donnees = ((input("Entrez deux nombres positifs : (exple, 72.19  35.28)  ")).strip()).split()
print("-------------------------")

# permet de créer sa propre "Exception" par instanciation de cette classe
class Exception_PERSONNELLE(Exception):
    pass


def affecte_donnees(donnees):
    return float(donnees[0]), float(donnees[1])


try:
    numerateur, denominateur = affecte_donnees(donnees)
    # on affecte les valeurs, récupérées dans la liste "donnees", aux 2 variables "numerateurs" et "denominateurs"
    # numerateur, denominateur = float(donnees[0]), float(donnees[1])     # on essaie de récupérer les données dans "numerateur" et "denominateur"
    
    if denominateur == 0:                                               # ici, on regarde si le "denominateur" est ègal à "0"
        raise ValueError("Le dénominateur ne doit pas être nul")        # et dans ce cas, on "déclenche" ("raise") volontairement une "Exception"
                                                                        # qui va être gérée au niveau de l'exception "ValueError"
    if numerateur == 0:                             # ici, on regarde si le numérateur est nul
        raise Exception_PERSONNELLE("Aïe, aïe, aïe : le numérateur est nul")  # !!! et dans ce cas, on crée un "Exception" PERSONNELLE  !!!  
                                                                        # en créant une instance à partir d'une classe "vide" (voir tout en haut !)

except IndexError as msg:   # ici, l'erreur provient de l'absence d'au moins une des deux valeurs
    print(" Il manque une ou deux des valeurs demandées ! ", msg)

except ValueError as msg:   # ici, deux problèmes différents peuvent apparaître avec la même exception "ValueError"
    if msg.args[0] == "Le dénominateur ne doit pas être nul":     # 1er problème : le "denominateur" vaut "0" (on a "déclenché" l'exception au dessus)
        print(str(msg) + "!")
    else:                                                         # 2nd problème : une des valeurs proposées n'est pas un nombre
        print("Les valeurs entrées doivent être des nombres ! (entiers ou réels) ", msg)

except Exception_PERSONNELLE as msg:
    print(msg)

except:             # ici, une erreur non prévue sera "gérée" par cette "exception" (A EVITER !!!)
    print("Une erreur est survenue... laquelle ?  On ne sait pas !")

else:               # Si aucune erreur n'est apparue dans les tests ci-dessus, on peut effectuer la division
    resultat = numerateur / denominateur
    print("Le résultat de la division vaut : ", resultat)
finally:            # et même si un problème est apparu précédemment, cette dernière ligne apparaîtra TOUJOURS !
    print("C'est fini !")



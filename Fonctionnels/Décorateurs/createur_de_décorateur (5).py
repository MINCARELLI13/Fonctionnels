print("")

# https://sametmarx.com/comprendre-les-decorateur-python-pas-a-pas-partie-2/

def createur_de_decorateur_avec_arguments(decorator_arg1, decorator_arg2):
    print("Je créé des décorateur et j'accepte des arguments:", decorator_arg1, decorator_arg2)

    def mon_decorateur(func):
        print("Je suis un décorateur, vous me passez des arguments:", decorator_arg1, decorator_arg2)

        # Ne pas mélanger les arguments du décorateurs et de la fonction !
        def wrapped(fonction_arg1, fonction_arg2) :
            print("Je suis le wrapper autour de la fonction décorée.\n"
                  "Je peux accéder à toutes les variables\n"
                  "\t- du décorateur: {0} {1}\n"
                  "\t- de l'appel de la fonction: {2} {3}\n"
                  "Et je les passe ensuite à la fonction décorée".format(decorator_arg1, decorator_arg2, fonction_arg1, fonction_arg2))
            func(fonction_arg1, fonction_arg2)

        return wrapped

    return mon_decorateur

@createur_de_decorateur_avec_arguments("Leonard", "Sheldon")    # remarquer les () après le décorateur !!!
def fonction_decoree_avec_arguments(function_arg1, function_arg2):
    print("Je suis une fonctions décorée, je ne me soucie que de mes arguments: {0}" 
           " {1}".format(function_arg1, function_arg2))


fonction_decoree_avec_arguments("Rajesh", "Howard")
#output:
#Je crée des décorateurs et j'accepte des arguments: Leonard Sheldon
#Je suis un décorateur, vous me passez des arguments: Leonard Sheldon
#Je suis le wrapper autour de la fonction décorée function.
#Je peux accéder à toutes les variables
#   - du décorateur: Leonard Sheldon
#   - de l'appel de la fonction: Rajesh Howard
#Et je les passe ensuite à la fonction décorée
#Je suis une fonction décorée, je ne me soucie que de mes arguments: Rajesh Howard
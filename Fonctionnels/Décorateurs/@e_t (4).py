# Au début, nous avons une fonction de base "gertie()" qui renvoie le message "Je lui ai appris à parler, Ecoute !"
# Le but est alors de construire le décorateur "@e_t" afin de modifier le résultat de la fonction "gertie()"
# et plus précisément de rajouter la phrase " : ...Maison ...Téléphone ...Maison" après celle de "gertie()"

# on construit le décorateur "@e_t" comme une fonction mais ayant comme argument func = "gertie()"
def e_t(func):
    print("func = ", func.__name__)         # on vérifie que l'argument de "@e_t" est bien "gertie()"
    # on définit alors la fonction "inner()" correspondant au décorateur "@e_t"
    # afin de lui faire exécuter une nouvelle tâche : ici, on rajoute une phrase "...Maison ...Téléphone ...Maison"
    # juste après la phrase de gertie
    def inner():
        return func() + " ...Maison ...Téléphone ...Maison"   # func() va renvoyer la phrase de gertie
    return inner

# La fonction "gertie()" renvoie le message "Je lui ai appris à parler, Ecoute !"
# On lui "associe" alors le décorateur "@e_t" qui va mofifier la fonction de base "gertie()"
@e_t
def gertie():
    return "Je lui ai appris à parler, Ecoute :"

@e_t
def elliot():
    return "J'ai l'impression qu'il répète toujours la même chose, non ? "

print("")
print(gertie())

print("")
print(elliot())

print

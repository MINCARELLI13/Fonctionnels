
print()

# Le but de ce script est de montrer comment protéger des attributs en lecture et en écriture
# pour cela on procède en 2 étapes :
#   1) on oblige tout accès à l'attribut "montant" à passer par "get_amount" et "set_amount" grâce à la méthode "property()"
#   2) à l'intérieur de la classe "User()", on utilise une variable protégée "__montant" (Attention aux 2 underscores !!!)

class User():

    def __init__(self, montant=0):
        self.montant = montant

    def get_amount(self):
        self.__montant = 2
        return self.__montant        # on renvoie la variable locale protégée "__montant" dont a bloqué la valeur à 2

    def set_amount(self, montant):
        self.__montant = 2      # on empêche tout modification du montant grâce à la variable locale protégée "__montant"
    
    montant = property(get_amount, set_amount)  # !!! on oblige tout accès à montant à passer par "get_amount" et "set_amount" !!!

# ----------------------------- main()
user = User(100)
user.montant += 10
print(user.montant)
user.montant += 20
print(user.montant)
    
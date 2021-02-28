

class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33       # ici, l'attribut "age" n'apparaît pas dans les paramètres de "__init__" mais il peut être mofifié comme les autres...
    
    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({}), prénom({}), âge({})".format(self.nom, self.prenom, self.age)
    
    def imprim(self):
        """Autre méthode plus classique"""
        return "Personne: nom({}), prénom({}), âge({})".format(self.nom, self.prenom, self.age)


p1 = Personne("Micado", "Jean")     # création de "p1", une instance de la class "Personne()"
print("")
print(p1)               # !!!  on affiche à l'écran le message "Personne: nom(Micado), prénom(Jean), âge(33)"
                        # car la fonction spéciale "__repr__" est faite spécifiquement pour cela  !!!  (idem pour "__str__")
p1.age = 44
print("")
print(repr(p1))         # ici, on peut obtenir le même réultat en se contentant d'appeler la méthode spéciale de l'objet passé en paramètre

p1.nom = "Zucchero"
print("")               
print(p1.imprim())      # Plus classique encore, on utilise une méthode créée pour l'occasion  :(





class Protege:

    """Classe possédant une méthode particulière d'accès à ses attributs :
        Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""
    def __init__(self):
        """On crée quelques attributs par défaut"""
        self.a = 1
        self.b = 2
        self.c = 3

    # La méthode spéciale "__getattr__" est appelée quand vous tapez objet.attribut(non pas pour modifier l'attribut mais simplement pour y accéder).
    # Python recherche l'attribut et, s'il ne le trouve pas dans l'objet et si une méthode__getattr__ existe, il va l'appeler en lui passant
    # en paramètre le nom de l'attribut recherché, sous la forme d'une chaîne de caractères.
    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé "nom", il appelle
            cette méthode, ce qui affiche une alerte"""   
        return "Alerte ! Il n'y a pas d'attribut '{}' ici !".format(nom)


pro = Protege()
print(pro.a)
print(pro.b)
print(pro.c)

print(pro.e)    # ici, l'attribut "e" n'existe pas pour l'objet "pro" et donc Python va chercher si une méthode "__getattr__" existe
                # pour voir si cette méthode permet d'accéder à cet attribut inconnu



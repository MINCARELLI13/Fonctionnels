

class Modification:

    def __init__(self, nom_val):
        self.nom = nom_val
        self.prenom = "Gérald"
    # La méthode spéciale "__setattr__" définit l'accès à un attribut destiné à être modifié !!!

    # Si vous écrivez "objet.nom_attribut = nouvelle_valeur", la méthode spéciale "__setattr__" sera appelée ainsi :
    # objet.__setattr__("nom_attribut", nouvelle_valeur)
    def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
            On se charge d'enregistrer l'objet"""        
        object.__setattr__(self, nom_attr, val_attr)    # !!! ne surtout pas écrire "self.attribut = valeur" sinon boucle infinie !!!
        # self.enregistrer()

modif = Modification("DUPONT")
print("")
print(modif.nom, modif.prenom)

modif.nom = "DURANT"
print("")
print(modif.nom, modif.prenom)



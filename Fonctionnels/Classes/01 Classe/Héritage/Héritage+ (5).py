# -*- coding: utf8 -*-

# la classe de base "Gaufre()" contient 1 attribut "sucre" initialisé à "2" par défaut
class Gaufre:
  def __init__(self, sucre):
    self.sucre = 2

# la sous-classe "GaufreGlacee" contient 2 attributs :
# un attribut "sucre" hérité de la classe de base, et un attribut glace propre à la sous-classe "GaufreGlacee"
class GaufreGlacee(Gaufre):
    def __init__(self, sucre_cuilleres, glace_cuilleres):
        super().__init__(sucre_cuilleres)       # on récupère les attributs de la classe de base (ici un seul : "sucre")
        self.sucre = sucre_cuilleres            # et on modifie la quantite de sucre qui était 2 par défaut dans la classe de base
        self.glace = glace_cuilleres


gaufre_glacee = GaufreGlacee(3, 1)
print("")
print("nombre de cuillères de sucre : ", gaufre_glacee.sucre)
print("nombre de cuillères de glace : ", gaufre_glacee.glace)
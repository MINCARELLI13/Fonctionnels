# -*- coding: utf8 -*-
import json
from math import *
import matplotlib.pyplot as plt


class BaseGraph:            # Voici la classe de base ou classe parent

    def __init__(self):
        self.title = "titre du graphe"
        self.x_label = "étiquette de l'axe des x"
        self.y_label = "étiquette de l'axe des y"
        plt.axis('equal')
        self.show_grid = True

    def show(self):

        # HERITAGE ! ! ! la méthode "xy_values()" appelée est systématiquement celle d'une des sous-classes "CosinusGraph" ou "SinusGraph"
        # car le "self." a pour nom "cosinus_graph" ou "sinus_graph" qui sont les objets créés à partir d'une de ces sous-classes
        x_values, y_values = self.xy_values()   
        plt.plot(x_values, y_values, '-', color = self.color)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()
        plt.close()
    
    def xy_values(self):            # HERITAGE ! le calcul des coorodnnés (x, y) se fera dans les sous classes avec le même nom de méthode
        raise NotImplementedError

class CosinusGraphe(BaseGraph): # HERITAGE ! on oublie pas de préciser la classe parent

    def __init__(self):
        super().__init__()      # HERITAGE !  on oublie pas d'importer les attributs de la classe parent
        self.title = "Tracé de la fonction cosinus"
        self.x_label = "axe des abscisses"
        self.y_label = "axe des ordonnées"
        self.color = "blue"

# cette méthode a le même nom que la méthode de la classe parent "BaseGraph()"
# et c'est elle qui sera utilisée lorsqu'on utilisera la méthode "show()" de la classe parent
    def xy_values(self):            
        x_values = [i*0.1 for i in range(0, 100)]
        y_values = [cos(i*0.1) for i in range(0, 100)]
        return (x_values, y_values)


class SinusGraphe(BaseGraph): # HERITAGE ! on oublie pas de préciser la classe parent

    def __init__(self):
        super().__init__()      # HERITAGE !  on oublie pas d'importer les attributs de la classe parent
        self.title = "Tracé de la fonction sinus"
        self.x_label = "axe des abscisses"
        self.y_label = "axe des ordonnées"
        self.color = "red"

# cette méthode a le même nom que la méthode de la classe parent "BaseGraph()"
# et c'est elle qui sera utilisée lorsqu'on utilisera la méthode "show()" de la classe parent
    def xy_values(self):
        x_values = [i*0.1 for i in range(0, 100)]
        y_values = [sin(i*0.1) for i in range(0, 100)]
        return (x_values, y_values)


def main():
    cosinus_graph = CosinusGraphe()     # initialisation de l'objet cosinus_graph de la sous-classe "CosinusGraphe()"
    cosinus_graph.show()                # calcul des coordonnées (x, y) et tracé du graphe de la fonction cosinus
                                        # par appel d'une méthode située exclusivement dans la classe de base "BaseGraph()" : HERITAGE !

    sinus_graph = SinusGraphe()         # initialisation de l'objet sinus_graph de la sous-classe "SinusGraphe()"
    sinus_graph.show()                  # calcul des coordonnées (x, y) et tracé du graphe de la fonction sinus
                                        # par appel d'une méthode située exclusivement dans la classe de base "BaseGraph()" : HERITAGE !

main()
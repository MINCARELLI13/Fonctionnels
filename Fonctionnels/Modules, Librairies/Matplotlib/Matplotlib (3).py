# -*- coding: utf8 -*-
import json
import time
import matplotlib.pyplot as plt
from math import *


plt.title("Trois lignes de couleurs")     # ajoute un titre au graphe
plt.axis('equal')                   # rend le repère orthonormal (unité des x = unité des y)
plt.xlabel("AXE DES ABSCISSES")     # étiquette affichant un texte horizontal sous l'axe des "x"
plt.ylabel("AXE DES ORDONNEES")     # étiquette affichant un texte vertical à gauche de l'axe des "y"

x = [i*0.1 for i in range(0, 100)]
y = [cos(i*0.1) for i in range(0, 100)]

x1 = [i*0.1 for i in range(0, 100)]
y1 = [sin(i*0.1) for i in range(0, 100)]

x2 = [i*0.1 for i in range(1, 100)]
y2 = [log(i*0.1) for i in range(1, 100)]

# "color" : "blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"
# "style" --> 4 sortes de lignes :  continue "-", tirets "--", points ":", tirets-points "-."
# "lw" = linewidth (épaisseur du trait)
plt.plot(x, y, '-', color = "blue", lw = 1)     # permet de tracer les droites de coordonnées (x,y) dans la fenêtre de tracé
plt.plot(x1, y1, '--', color = "green", lw = 2)   # permet de tracer les droites de coordonnées (x1,y1) dans la fenêtre de tracé
plt.plot(x2, y2, ':', color = "red", lw = 3)    # permet de tracer les droites de coordonnées (x2,y2) dans la fenêtre de tracé
plt.grid (True)         # permet d'avoir une grille de fond

plt.show()      # permet d’afficher un graphique dans une fenêtre de tracé
plt.close()     # permet de fermer la fenêtre de tracé

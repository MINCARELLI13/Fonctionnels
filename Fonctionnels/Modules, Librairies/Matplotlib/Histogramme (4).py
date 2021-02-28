import matplotlib.pyplot as plt  # Avec Matplotlib, nous créons des graphiques grâce à l'objet matplotlib.pyplot, que l'on nomme souvent "plt"
import numpy as np

# on dispose d'un tableau contenant une série d'âges
ages = [25, 65, 26, 26, 46, 37, 36, 36, 28, 28, 57, 37, 48, 48, 37, 28, 60, 25, 65, 46, 26, 46, 37, 36, 37, 29, 58, 47, 47, 48, 48, 47, 48, 60]

# crée un unique graphique par fenêtre (= plt.subplot())
un_graphe = plt.subplot()

# le graphique est représenté sous forme d'histogramme (= .hist())
un_graphe.hist(ages)

plt.title("Histogramme des âges")

plt.show()




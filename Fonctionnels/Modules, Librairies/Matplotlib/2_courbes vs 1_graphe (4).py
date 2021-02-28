import matplotlib.pyplot as plt  # Avec Matplotlib, nous créons des graphiques grâce à l'objet matplotlib.pyplot, que l'on nomme souvent "plt"
import numpy as np

# calcule les ordonnées de la fonction exponentielle amortie
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

# génère une plage d'abscisses de x=0 à x=5 par pas de 0.05
t1 = np.arange(0.0, 5.0, 0.05)

# 2 courbes sur un même graphique

plt.plot(t1, f(t1), "b-")       # on trace la première courbe

plt.plot(t1, np.cos(2*np.pi*t1), "r--")     # puis la seconde courbe

plt.show()




import matplotlib.pyplot as plt
import seaborn as sns

# crée un unique graphe dans la fenêtre
un_graphe = plt.subplot()

# le repère devient orthonormée
un_graphe.axis("equal")

# 
un_graphe.pie([24, 18, 11],
            labels = ["Femmes", "Hommes", "Autres"],
            autopct="%1.3f pourcents")          # le "%" sera remplacé par les valeurs respectives des pourcentages

# ajoute un titre au graphe
plt.title("Un superbe camembert")

plt.show()
# -*- coding: utf8 -*-
#!/usr/bin/python

import numpy as np
import pandas as pd

print("")
print("-----------------------------------------------------------------------------------------------------------------------------")

# on crée un tableau_python
maman_panda_py = [100, 5, 20, 80]      # où 100, 5, 20 et 80 sont respectvt les tailles des pattes, poil, queue et ventre
bebe_panda_py = [50, 2.5, 10, 40]
papa_panda_py = [110, 6, 22, 80]
famille_panda_py = [maman_panda_py, bebe_panda_py, papa_panda_py]
print("-------------------------------------------------------------------------")
print("famille_panda_py :")
print(famille_panda_py)

print("")

# Création du tableau_pandas 'simple' grâce à la méthode ".DataFrame()"
print("-------------------------------------------------------------------------")
famille_panda_pd = pd.DataFrame(famille_panda_py)
print("famille_panda_pd 'SIMPLE' :")
print(famille_panda_pd)

# On utilise exactement la même méthode pour créer un tableau_pandas à partir d'un tableau_numpy
# famille_panda_pd = pd.DataFrame(famille_panda_np)   où "famille_panda_np" est un "tableau numpy"

print("")

# Création du tableau_pandas grâce à la méthode ".DataFrame()"
# mais avec les otpions "index" (= lignes) et "columns" (= colonnes)
print("-------------------------------------------------------------------------")
famille_panda_pd = pd.DataFrame(famille_panda_py, index=["maman", "bebe", "papa"], columns=["pattes", "poil", "queue", "ventre"])
print("famille_panda_pd 'AVEC INDEX et COLUMNS' :")
print(famille_panda_pd)

# On utilise exactement la même méthode pour créer un tableau_pandas à partir d'un tableau_numpy
# famille_panda_pd = pd.DataFrame(famille_panda_np, index=["maman", "bebe", "papa"], columns=["pattes", "poil", "queue", "ventre"])
# où "famille_panda_np" est un "tableau numpy"

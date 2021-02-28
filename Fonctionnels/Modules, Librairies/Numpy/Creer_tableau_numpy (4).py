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
print("-------------------------------------------------------------------------")
# Création du tableau_numpy grâce à la méthode "np.array()"
famille_panda_np = np.array(famille_panda_py)
print("famille_panda_np :")
print(famille_panda_np)

# On utilise exactement la même méthode pour créer un tableau_numpy à partir d'un tableau_pandas
# famille_panda_np = pd.DataFrame(famille_panda_pd)   où "famille_panda_pd" est un "tableau pandas"



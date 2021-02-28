# -*- coding: utf8 -*-
import time

def Test():
    "-".join(str(n) for n in range(1925000))

temps = []                  # on crée une liste pour enregistrer les temps des 10 tests effectués
                            # pour mesurer le traitement de la fonction "Test"
for i in range(10):
    debut = time.time()     # on débute la mesure du temps mit pour exécuter le code "Test"
    Test()                  # on lance le code "Test"
    fin = time.time()       # on arrête la mesure après avoir exécuté le code "Test"
    interval = fin-debut    # on calcule l'intervalle de temps
    temps.append(interval)

print("Moyenne de temps : ", sum(temps)/len(temps))



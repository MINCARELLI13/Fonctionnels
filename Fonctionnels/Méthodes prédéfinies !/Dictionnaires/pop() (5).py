# -*- coding: utf8 -*-

# une liste possédant 2 dictionnaires de 19 attributs chacun
dict = [{"neuroticism": -0.0739192627121713, "language": "Shona", "longitude": 29.798455535838603, "latitude": -19.922097800281783, "country_tld": "zw", "age": 12,
    "income": 333, "sex": "Male", "religion": "syncretic", "extraversion": 1.051833688742943,
    "date_of_birth": "2005-01-10", "agreeableness": 0.1441229877537559, "id_str": "LB3-3Cl", "conscientiousness": 0.2419104411765549,
    "internet": "false", "country_name": "Zimbabwe", "openness": -0.024607605122172617, "id": 6636726630}, {"neuroticism": -0.255,
    "language": "Shona", "longitude": -0.255, "latitude": -0.257, "country_tld": "zw", "age": -0.255, "income": -0.255, "sex": "Male",
    "religion": "syncretic","extraversion": -0.255, "date_of_birth": "2005-01-10", "agreeableness": 0.1441229877537559,
    "id_str": "LB3-3Cl", "conscientiousness": -0.255, "internet": "false", "country_name": "Zimbabwe", "openness": -0.255,
    "id": -0.255}] 

# le but est de supprimer les 2 clés "longitude" et "latitude" et de les remplacer par l'objet "Position" qui les contiendra

class Position:                     # création de la class "Position"

    def __init__(self, longitude_val, latitude_val):
        self.longitude = longitude_val
        self.latitude = latitude_val
    
for dico in dict:                                   # on récupère chacun des 2 dicos dans la liste "dict"
    latitude_recup = dico.pop("latitude")           # on supprime la "latitude" (clé, valeur) et on récupère la valeur dans "latitude_recup"
    longitude_recup = dico.pop("longitude")         # on supprime la "longitude" (clé, valeur) et on récupère la valeur dans "longitude_recup"
    coordonnees = Position(longitude_recup, latitude_recup)     # on crée l'objet "coordonnees" qui va contenir les anicennes valeurs de "longitude et "latitude
    print()
    print(dico, " / ",coordonnees.longitude, " / ", coordonnees.latitude)       # on "print" les coordonnées récupérée après les avoir
                                                                                # supprimé de chaque dictionnaire "dico"
    print()
    
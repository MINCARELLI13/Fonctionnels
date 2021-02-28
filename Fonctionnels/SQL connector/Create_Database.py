import mysql.connector

config = {'user': 'root', 'password': '123ab456', 'host': 'localhost', 'charset': 'utf8'}

cnx = mysql.connector.connect(**config)
        # créer un curseur de base de données pour effectuer des opérations SQL
cursor = cnx.cursor()
        # création de la BDD Test
query = "CREATE DATABASE IF NOT EXISTS TEST"
cursor.execute(query)
        # utilisation de la BDD Test
query = "USE TEST"
cursor.execute(query)
        # arrêt de la connection avec SQL
cnx.close()

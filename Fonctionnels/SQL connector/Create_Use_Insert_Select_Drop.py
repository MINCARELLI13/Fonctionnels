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
        # création de la Table Tototata
query = "CREATE TABLE IF NOT EXISTS Tototata (id Int Primary Key Auto_increment, Pile Char(3), Face Char(3)) Engine=InnoDB"
cursor.execute(query)
        # insertion des données
query = "INSERT INTO TotoTata (Pile, Face) VALUES (%s, %s)"
value = [('OUI','OUI'), ('OUI','NON'), ('NON','OUI'), ('NON','NON')]
cursor.executemany(query, value)
cnx.commit()
        # insertion des données
query = "SELECT Pile, Face FROM Tototata order by id"
cursor.execute(query)
for (rep1, rep2) in cursor:
    print(rep1, rep2)
        # suppression de la BDD Test
query = "DROP DATABASE Test"
cursor.execute(query)
cnx.close()

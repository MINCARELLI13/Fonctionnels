import mysql.connector

print()

cnx = mysql.connector.connect(user = 'root',
                            password = '123ab456',
                            host = 'localhost',
                            database = 'BDD_OFF')

cursor = cnx.cursor()
query = "SELECT id, Pile, Face FROM Tototata order by id"
cursor.execute(query)

for (id, rep1, rep2) in cursor:
    print(id, rep1, rep2)

print()
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='liga')

cursor = cnx.cursor()

query = ("SELECT nombre FROM equipo where puesto=3;")
data = cursor.execute(query)
print(data)
     


cnx.close()
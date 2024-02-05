import mysql.connector

db = None

try:
    db = mysql.connector.connect(host='localhost',
                                   database='LaPlateforme',
                                   user='root',
                                   password='root')
    cursor = db.cursor()
    cursor.execute("SELECT nom, capacite FROM salle")
    salles = cursor.fetchall()    
    print(salles)

except mysql.connector.Error as e:
    print(e)

finally:
    if db is not None and db.is_connected():
        cursor.close()
        db.close()
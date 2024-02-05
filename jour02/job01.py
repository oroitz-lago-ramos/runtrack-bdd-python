import mysql.connector

db = None

try:
    db = mysql.connector.connect(host='localhost',
                                   database='LaPlateforme',
                                   user='root',
                                   password='root')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM etudiant")
    etudiants = cursor.fetchall()    
    print(etudiants)

except mysql.connector.Error as e:
    print(e)

finally:
    if db is not None and db.is_connected():
        cursor.close()
        db.close()
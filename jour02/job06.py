import mysql.connector

db = None

try:
    db = mysql.connector.connect(host='localhost',
                                   database='LaPlateforme',
                                   user='root',
                                   password='root')
    cursor = db.cursor()
    cursor.execute("SELECT capacite FROM salle")
    capacites = cursor.fetchall()    
    capacite_totale = 0
    for i in capacites:
        capacite_totale += i[0]
    print(f"La capacité de toutes les salles est de: {capacite_totale}")

except mysql.connector.Error as e:
    print(e)

finally:
    if db is not None and db.is_connected():
        cursor.close()
        db.close()
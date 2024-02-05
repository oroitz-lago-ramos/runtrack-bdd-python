import mysql.connector

db = None

try:
    db = mysql.connector.connect(host='localhost',
                                   database='LaPlateforme',
                                   user='root',
                                   password='root')
    cursor = db.cursor()
    cursor.execute("SELECT superficie FROM etage")
    superficies = cursor.fetchall()    
    superficie_totale = 0
    for i in superficies:
        superficie_totale += i[0]
    print(f"La superficie de La Plateforme est de {superficie_totale} m²")

except mysql.connector.Error as e:
    print(e)

finally:
    if db is not None and db.is_connected():
        cursor.close()
        db.close()
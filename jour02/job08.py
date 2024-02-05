import mysql.connector

class Database:
    def __init__(self) -> None:
        self.host = "localhost",
        self.user = "root",
        self.password = "root",
        self.database = "zoo"
    
    def connect(self):
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db.cursor()
        
    def disconnect(self):
        if self.db.is_connected():
            self.cursor.close()
            self.db.close()
    
    def execute(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        self.db.commit()
        self.disconnect()
    
    def fetch(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        result = self.cursor.fetchall()
        self.disconnect()
        return result
    
    
class Main:
    def __init__(self) -> None:
        #Cette classe devra demander au directeur du zoo d'ajouter supprimer modifier des cages ou des animaux
        # Afficher l’ensemble des animaux présents dans le zoo ainsi que la liste des animaux présents dans les cages.
        # Calculer la superficie totale de toutes les cages
        self.animal = Animal()
        self.cage = Cage()
    
    
    def run(self):
        self.ask_user()
        choice = int(input("Entrez votre choix: "))
        if choice == 1:
            self.add_cage()
        elif choice == 2:
            self.add_animal()
        elif choice == 3:
            self.modify_cage()
        elif choice == 4:
            self.modify_animal()
        elif choice == 5:
            self.remove_cage()
        elif choice == 6:
            self.remove_animal()
        elif choice == 7:
            self.show_animals()
        elif choice == 8:
            self.superficie_totale()
        elif choice == 9:
            self.capacite_totale()
        else:
            print("Choix invalide")    
    def ask_user(self):
        print("1. Ajouter une cage")
        print("2. Ajouter un animal")
        print("3. Modifier une cage")
        print("4. Modifier un animal")
        print("5. Supprimer une cage")
        print("6. Supprimer un animal")
        print("7. Afficher l'ensemble des animaux d'une cage donnée")
        print("8. Afficher la superficie totale de toutes les cages")
        print("9. Afficher la capacité totale de toutes les cages")
        
    def add_cage(self):
        superficie = int(input("Entrez la superficie: "))
        capacite = int(input("Entrez la capacité: "))
        self.cage.add(superficie, capacite)
        
    def add_animal(self):
        nom = input("Entrez le nom: ")
        age = int(input("Entrez l'age: "))
        race = input("Entrez la race: ")
        pays = input("Entrez le pays: ")
        id_cage = int(input("Entrez l'id de la cage: "))
        naissance = input("Entrez la date de naissance: ")
        
    def modify_cage(self):
        pass
    def modify_animal(self):
        pass
    def remove_cage(self):
        id = int(input("Entrez l'id de la cage: "))
        self.cage.remove(id)
        
        
    def remove_animal(self):
        id = int(input("Entrez l'id de l'animal: "))
        self.animal.remove(id)
        
    def show_all(self):
        print("Cages")
        cages = self.cage.show_all()
        for cage in cages:
            print(cage)
        print("Animaux")
        animaux = self.animal.show_all()
        for animal in animaux:
            print(animal)
            
    def show_animals(self):
        id = int(input("Entrez l'id de la cage: "))
        animaux = self.cage.show_animals(id)
        print("Dans la cage {id} il y a:")
        for animal in animaux:
            print(animal)
            
    def superficie_totale(self):
        print(self.cage.superficie_totale())
        
    def capacite_totale(self):
        print(self.cage.capacite_totale())
    
    
class Animal:
    def __init__(self) -> None:
        self.table = "animal"
        self.db = Database()
    def add(self, nom, age, race, pays, id_cage, naissance):
        query = f"INSERT INTO {self.table} (nom, race, pays, id_type_cage, naissance) VALUES (%s, %s, %s, %s, %s)"
        params = (nom, age, race, pays, id_cage, naissance)
        self.db.execute(query, params)
    def modify_age(self, id,age):
        query = f""
        
    def modify_all(self, id, nom, age,race,pays,id_cage,naissance):
        pass
    
    def modify_cage(self, id, id_cage):
        pass
    
    def modify_name(self, id, nom):
        pass
    
    def show_all(self):
        query = f"SELECT * FROM {self.table}"
        return self.db.fetch(query)
    def remove(self,id):
        query = f"DELETE FROM {self.table} WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
        

class Cage:
    def __init__(self) -> None:
        self.table = "cage"
        self.db = Database()
    
    def add(self, superficie, capacite):
        query = f"INSERT INTO {self.table} (superficie, capacite) VALUES (%s, %s)"
        params = (superficie, capacite)
        self.db.execute(query, params)
    
    def modify_superficie(self, id, superficie):
        query = f"UPDATE {self.table} SET superficie = %s WHERE id = %s"
        params = (superficie, id)
        self.db.execute(query, params)
        
    def modify_capacite(self, id, capacite):
        query = f"UPDATE {self.table} SET capacite = %s WHERE id = %s"
        params = (capacite, id)
        self.db.execute(query, params)
    
    def modify_all(self, id, superficie, capacite):
        query = f"UPDATE {self.table} SET superficie = %s, capacite = %s WHERE id = %s"
        params = (superficie, capacite, id)
        self.db.execute(query, params)
    
    def show_all(self):
        query = f"SELECT * FROM {self.table}"
        return self.db.fetch(query)
    
    def remove(self, id):
        query = f"DELETE FROM {self.table} WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
    
    def show_animals(self, id):
        query = f"SELECT * FROM animal WHERE id_type_cage = %s"
        params = (id,)
        return self.db.fetch(query, params)
    
    def superficie_totale(self):
        query = f"SELECT SUM(superficie) FROM {self.table}"
        return self.db.fetch(query)
    
    def capacite_totale(self):
        query = f"SELECT SUM(capacite) FROM {self.table}"
        return self.db.fetch(query)
    
main_app = Main()
main_app.run()
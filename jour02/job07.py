import mysql.connector

class Employe:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='Entreprise'
        )
        self.cursor = self.mydb.cursor()
    def insert_employee(self, nom, prenom, salaire, id_service):
        query = '''
            INSERT INTO employe (nom, prenom, salaire, id_service) 
            VALUES (%s, %s, %s, %s)
        '''
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.mydb.commit()
    def get_employee_by_id(self, employee_id):
        query = 'SELECT * FROM employe WHERE id = %s'
        values = (employee_id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def get_all_employees(self):
        query = 'SELECT * FROM employe'
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def get_high_salary_employees(self):
        query = 'SELECT * FROM employe WHERE salaire > 3000.00'
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def update_employee_salary(self, employee_id, new_salary):
        query = 'UPDATE employe SET salaire = %s WHERE id = %s'
        values = (new_salary, employee_id)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_employee(self, employee_id):
        query = 'DELETE FROM employe WHERE id = %s'
        values = (employee_id,)
        self.cursor.execute(query, values)
        self.mydb.commit()
    def close_connection(self):
        self.cursor.close()
        self.mydb.close()

employe = Employe()
print(employe.delete_employee(5))
print(employe.get_all_employees())
employe.insert_employee("Rigaud","Pierre-Louis", 5304, 4)
print(employe.get_all_employees())

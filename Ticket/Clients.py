from Users import Users
import sqlite3

class Clients(Users):
    def __init__(self,id_code:str):
        self.id_code = id_code
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT id_code FROM Clients WHERE id_code   =?''', (self.id_code,))
        client = cursor.fetchone()
        if client is None:
            cursor.execute('''INSERT INTO Clients (id_code, event) VALUES (?, ?)''',(self.id_code, None))
            conn.commit()
            return
        else:
            return

"""add_client()""" #TODO:DONE
# C = Clients(1)
# C = Clients(11)
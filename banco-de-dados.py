from os import curdir
import sqlite3

class SQliteDBConnector:
    def __init__(self, db_filename):
        dbname = "database.db"

    # Cria nova tabela
    def create_new(self, db_filename):
        conn = sqlite3.connect(db_filename)

        cursor = conn.cursor()
        cursor.execute("CREATE TABLE usuarios(id INT PRIMARY KEY, username TEXT, password TEXT);")
        cursor.execute("INSERT INTO usuarios VALUES (1, 'admin', 'adminpass');")
        cursor.execute("INSERT INTO usuarios VALUES (2, 'user', 'password');")

        cursor.execute("CREATE TABLE cadastro (cpf INT PRIMARY KEY, id FOREIGN KEY, nome TEXT, datanasc INT, telefone INT);")
        cursor.execute("INSERT INTO cadastro VALUES (00000000000, 1, 'deus', 0, 9999999999);")

        cursor.commit()
        conn.close()

    def create_user():
        print("cria usuario")

    # Conecta ao banco, padrao database.db
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.dbname)
        except:
            print("Falha ao conectar ao DB")

    def disconnect(self):
        try:
            self.conn.close()
        except:
            prit("Falha ao desconectar")

def listDB():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM usuarios;''')
    conn.commit()
    for row in cursor.fetchall():
        print(row)
    
    conn.close()


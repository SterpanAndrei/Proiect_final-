import sqlite3

def create_connection():
    return sqlite3.connect('Biblioteca.db')

def init_db():
    connection = sqlite3.Connection('Biblioteca.db')
    cursor = connection.cursor()

    sql_script = """
    CREATE TABLE IF NOT EXISTS Carti (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Titlu VARCHAR(50) NOT NULL,
        Autor VARCHAR(30) NOT NULL,
        Gen  VARCHAR(30),
        Status VARCHAR(20) DEFAULT 'Disponibil'
    );
    
    CREATE TABLE IF NOT EXISTS Cititori (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nume VARCHAR(30) NOT NULL,
        Varsta INTEGER,
        Telefon VARCHAR(20) NOT NULL UNIQUE
    );
    """
    cursor.executescript(sql_script)

    connection.commit()

    connection.close()
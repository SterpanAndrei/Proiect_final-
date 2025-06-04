from db_biblioteca import create_connection
from Class_OOP_Biblioteca import Carte,Cititor


def adauga_carte(carte:Carte):
    baza_de_date = create_connection()
    baza_cursor = baza_de_date.cursor()
    baza_cursor.execute("""
    INSERT INTO Carti (Titlu, Autor, Gen, Status)
    VALUES ( ?, ?, ?, ? )
    """,(carte.titlu, carte.autor, carte.gen, carte.status))

    baza_de_date.commit()

    baza_de_date.close()


def afiseaza_carti():
    baza_de_date = create_connection()
    baza_cursor = baza_de_date.cursor()
    baza_cursor.execute("SELECT * FROM Carti")
    carti = baza_cursor.fetchall()

    baza_de_date.close()
    return carti


def sterge_carte(id_carte):
    baza_de_date = create_connection()
    baza_cursor = baza_de_date.cursor()
    baza_cursor.execute("DELETE FROM Carti WHERE ID =?", (id_carte,))

    baza_de_date.commit()

    baza_de_date.close()


def imprumuta_carte(id_carte):
    baza_de_date = create_connection()
    baza_cursor = baza_de_date.cursor()
    baza_cursor.execute("UPDATE Carti SET Status = 'imprumutata' WHERE ID=?", (id_carte,))

    baza_de_date.commit()

    baza_de_date.close()


def returneaza_carte(id_carte):
    baza_de_date = create_connection()
    baza_cursor = baza_de_date.cursor()
    baza_cursor.execute("UPDATE SET Status = 'disponibila' WHERE ID=?", (id_carte,))

    baza_de_date.commit()

    baza_de_date.close()


def procesare_cititor(cititor:Cititor):
    baza_de_date = create_connection()
    baza_cursor = baza_de_date.cursor()
    baza_cursor.execute("""
    INSERT INTO Cititori (Nume, Telefon, Varsta)
    VALUES (?, ?, ?)
    """, (cititor.nume, cititor.telefon, cititor.vastra))

    baza_de_date.commit()

    baza_de_date.close()


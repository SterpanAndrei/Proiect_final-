from xml.dom.minidom import ProcessingInstruction

from db_biblioteca import init_db
from Class_OOP_Biblioteca import Carte, Cititor
from CRUD_Biblioteca import *

def meniu():
    print("<<<<< MENIUL BIBLIOTECII >>>>>")
    print("1. Inregistrare cititor")
    print("2. Adauga carte")
    print("3. Afiseaza lista cartilor")
    print("4. Imprumutare carte")
    print("5. Returnare carte")
    print("6. Stergere carte")
    print("x Iesire")
    return input("Alege o optiune: \n")


def executare_biblioteca():
    init_db()
    while True:
        optiune = meniu()
        if optiune =="1":
            nume = input("Nume: ")
            telefon = input("Nr. telefon: ")
            varsta = input("Varsta: ")
            cititor = Cititor(nume,telefon, varsta)
            procesare_cititor(cititor)
            print(f"Persoana {nume} a fost inregistrata cu succes.")
        elif optiune == "2":
            titlu = input("Titlu: ")
            autor= input("Autor: ")
            gen = input("Gen: ")
            carte = Carte(titlu, autor, gen)
            adauga_carte(carte)
            print("Cartea a fost adaugata cu succes.")
        elif optiune =="3":
            for carte in afiseaza_carti():
                print(carte)
        elif optiune == "4":
            id_carte = int(input("ID carte imprumutata: "))
            imprumuta_carte(id_carte)
            print("Cartea a fost imprumutata.")
        elif optiune =="5":
            id_carte = int(input("ID carte returnata: "))
            returneaza_carte(id_carte)
            print("Cartea a fost returnata.")
        elif optiune == "6":
            id_carte = int(input("ID casrte de sters: "))
            sterge_carte(id_carte)
            print("Cartea a fost stearsa.")
            break
        else:
            print("Valoare incorecta.")

if __name__ == "__main__":
    executare_biblioteca()
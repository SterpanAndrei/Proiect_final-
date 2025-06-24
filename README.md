Biblioteca Virtuală – Aplicație de gestionare cărți și cititori

    Acest proiect este o aplicație în Python care simulează o bibliotecă digitală de bază.  
    Utilizatorul poate gestiona cititori, cărți și împrumuturi, cu datele salvate într-o bază de date locală `SQLite`.



  Ce face aplicația?

    - Permite **înregistrarea cititorilor** (nume, telefon, vârstă)
    - Permite **adăugarea de cărți** (titlu, autor, gen)
    - Afișează lista completă a cărților înregistrate
    - Oferă opțiuni de **împrumut** și **returnare** a cărților
    - Actualizează automat statusul cărților (`Disponibil` / `Împrumutat`)
    - Permite **ștergerea cărților**
    - Include un **meniu interactiv** în terminal



Clase folosite

  Aplicația este structurată pe principiile OOP, iar clasele principale sunt:

    => Carte
	Reprezintă o carte din bibliotecă.
	- Atribute: `titlu`, `autor`, `gen`, `status`

    => Cititor
	Reprezintă un cititor înregistrat.
	- Atribute: `nume`, `telefon`, `varsta`



    Structura fișierelor
        Proiect_final-/
        ├── Executare_Biblioteca.py # Meniul și funcțiile principale
        ├── Class_OOP_Biblioteca.py # Clasele Carte și Cititor
        ├── CRUD_Biblioteca.py # Operații cu baza de date (adăugare, ștergere etc.)
        ├── db_biblioteca.py # Inițializare baza de date (SQLite)
        └── Biblioteca.db # Fișierul SQLite creat automat




  Cum rulează aplicația

    Pentru a rula aplicația, deschid un terminal în directorul proiectului și scriu comanda:

	 python Executare_Biblioteca.py


   La rulare, aplicația inițializează automat baza de date și afișează meniul de opțiuni. Eu aleg o opțiune tastând cifra corespunzătoare și apoi introduc datele cerute (de exemplu, când adaug o carte sau un cititor).

   Pentru a ieși din aplicație, tastăm x când suntem în meniul principal.

  Exemplu de interacțiune:

    <<<<< MENIUL BIBLIOTECII >>>>>
    1. Inregistrare cititor
       2. Adauga carte
       3. Afiseaza lista cartilor
       4. Imprumutare carte
       5. Returnare carte
       6. Stergere carte
       x Iesire
    
    
    Alege o optiune: 2
    
    Titlu: Enigma Otiliei
    
    Autor: George Călinescu
    
    Gen: Roman
    
    Cartea a fost adăugată cu succes.

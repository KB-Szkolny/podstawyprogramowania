name = input("Enter name: ")  # Wypisuje komunikat proszący użytkownika o wpisanie imienia i przypisuje wpisany tekst do zmiennej name
if name[-1] == 'a':  # Sprawdza warunek: czy ostatni znak imienia (name[-1]) jest równy literze 'a'
    print(f'{name} - Polish female name')  # Jeśli warunek jest prawdziwy, wypisuje że imię to polskie imię żeńskie
else:  # Jeśli warunek jest fałszywy, czyli imię nie kończy się na 'a'
    print(f'{name} - Not female')  # Wypisuje że imię nie jest żeńskie
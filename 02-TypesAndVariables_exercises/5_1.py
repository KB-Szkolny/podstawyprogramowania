first_name = input('Enter your first name: ')   # Pobiera imię od użytkownika jako tekst (str)
last_name = input('Enter your last name: ')    # Pobiera nazwisko od użytkownika jako tekst (str)

full_name = first_name + ' ' + last_name    # Łączy (konkatenuje) imię, spację i nazwisko w jeden ciąg znaków

print(f'Your first name is {first_name} and your last name is {last_name}') # Wypisuje imię i nazwisko osobo z użyciem f-stringa
print(f'And your full name is {full_name}')     # Wypisuje połączone pełne imię i nazwisko
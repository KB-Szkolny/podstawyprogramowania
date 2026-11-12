age = int(input('Enter age: '))   #Pobiera wiek od użytkownika i zmienia go na liczbę całkowitą (int)
no_tax = age < 27   # Sprawdza czy wiek jest mniejszy niż 27 (zwraca True lub False)
print(f'Exemption from paying taxes: {no_tax}')  # Wypisuje wynik
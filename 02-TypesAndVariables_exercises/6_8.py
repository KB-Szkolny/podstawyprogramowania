first = input('Enter first letter: ')        # Pobiera pierwszą literę od użytkownika
last = input('Enter last letter: ')          # Pobiera drugą literę od użytkownika

first_letter_code = ord(first)              # Zamienia pierwszą literę na jej kod liczbowy (ASCII)
last_letter_code = ord(last)                # Zamienia drugą literę na jej kod liczbowy (ASCII)

number_of_letters = ord(last) - ord(first) - 1  # Oblicza ilość liter pomiędzy (odejmuje kody i skrajną literę)

print(f'Between {first} and {last} is {number_of_letters} letters')  # Wypisuje końcowy wynik
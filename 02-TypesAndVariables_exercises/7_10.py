import random  # Importuje moduł 'random' do generowania liczb losowych

# COMPUTER TURN
computer = random.randint(1, 6)  # Komputer losuje liczbę od 1 do 6

# YOUR TURN
you = int(input('Enter your guess (1-6): '))  # Pobiera odpowiedź i zamienia ją na liczbę całkowitą (int)

you_won = you == computer  # Sprawdza czy wybór jest równy wylosowanej liczbie (zwraca True lub False)

print(f'You won: {you_won}')  # Wypisuje wynik (True jeśli odgadłeś, False - nie odgadłeś)
###
# A simple number guessing game
#
import random  # Importuje moduł random, który umożliwia generowanie liczb losowych

# Randomly chosen number to be guessed from 1 to 100  # Losowo wybrana liczba do zgadnięcia od 1 do 100
number_to_guess = random.randint(1, 100)  # Generuje losową liczbę całkowitą z zakresu 1-100 i przypisuje do zmiennej number_to_guess
user_guess = 0  # Przypisuje wartość 0 do zmiennej user_guess, która będzie przechowywać zgadywaną liczbę użytkownika

print("Guess the number between 1 and 100!")  # Wypisuje komunikat zachęcający użytkownika do zgadywania liczby

while user_guess != number_to_guess:  # Rozpoczyna pętlę, która wykonuje się dopóki zgadywana liczba (user_guess) jest różna od liczby do zgadnięcia (number_to_guess)
    user_guess = int(input("Enter your guess: "))  # Wypisuje komunikat proszący użytkownika o wpisanie zgadywanej liczby, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej user_guess

    if user_guess < number_to_guess:  # Sprawdza warunek: czy zgadywana liczba (user_guess) jest mniejsza niż liczba do zgadnięcia (number_to_guess)
        print("Too low! Try again.")  # Jeśli warunek jest prawdziwy, wypisuje że liczba jest za mała i prosi o ponowną próbę
    elif user_guess > number_to_guess:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy zgadywana liczba jest większa niż liczba do zgadnięcia
        print("Too high! Try again.")  # Jeśli warunek jest prawdziwy, wypisuje że liczba jest za duża i prosi o ponowną próbę
    else:  # Jeśli żaden z powyższych warunków nie jest prawdziwy, czyli zgadywana liczba jest równa liczbie do zgadnięcia
        print("Congratulations! You guessed the correct number.")  # Wypisuje gratulacje za poprawne zgadnięcie liczby
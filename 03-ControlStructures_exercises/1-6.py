###
# Checking whether the number
# entered from the keyboard is even or odd
#
number = int(input('Enter number: '))  # Wypisuje komunikat proszący użytkownika o wpisanie liczby, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej number

if number % 2 == 0:  # Sprawdza warunek: czy reszta z dzielenia liczby (number) przez 2 jest równa 0, czyli czy liczba jest parzysta
    print(f'{number} is even')  # Jeśli warunek jest prawdziwy, wypisuje że liczba jest parzysta
else:  # Jeśli warunek (number % 2 == 0) jest fałszywy, czyli liczba jest nieparzysta
    print(f'{number} is odd')  # Wypisuje że liczba jest nieparzysta
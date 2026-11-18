number = int(input('Enter a number: '))  # Wypisuje komunikat proszący użytkownika o wpisanie liczby, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej number

if number >= 1:  # Sprawdza warunek: czy liczba (number) jest większa lub równa 1
    print(f'Number {number} is positive')  # Jeśli warunek jest prawdziwy, wypisuje że liczba jest dodatnia
elif number <= -1:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy liczba jest mniejsza lub równa -1
    print(f'Number {number} is negative')  # Jeśli warunek jest prawdziwy, wypisuje że liczba jest ujemna
elif number == 0:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy liczba jest równa 0
    print('Number is 0')  # Jeśli warunek jest prawdziwy, wypisuje że liczba jest równa 0
else:  # Jeśli żaden z powyższych warunków nie jest prawdziwy, czyli użytkownik wpisał coś niepoprawnego
    print('You typed something wrong')  # Wypisuje komunikat o niepoprawnym wpisaniu

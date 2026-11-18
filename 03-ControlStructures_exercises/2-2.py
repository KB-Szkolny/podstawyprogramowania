###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')  # Wypisuje komunikat proszący użytkownika o wpisanie symbolu rozmiaru i przypisuje wpisany tekst do zmiennej size

if size == 'S':  # Sprawdza warunek: czy symbol rozmiaru (size) jest równy 'S'
    print('S: Small size')  # Jeśli warunek jest prawdziwy, wypisuje opis rozmiaru Small
elif size == 'M':  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy symbol rozmiaru jest równy 'M'
    print('M: Medium size')  # Jeśli warunek jest prawdziwy, wypisuje opis rozmiaru Medium
elif size == 'L':  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy symbol rozmiaru jest równy 'L'
    print('L: Large size')  # Jeśli warunek jest prawdziwy, wypisuje opis rozmiaru Large
elif size == 'XL':  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy symbol rozmiaru jest równy 'XL'
    print('XL: Extra large size')  # Jeśli warunek jest prawdziwy, wypisuje opis rozmiaru Extra Large
else:  # Jeśli żaden z powyższych warunków nie jest prawdziwy, czyli symbol jest niepoprawny
    print('Incorrect symbol')  # Wypisuje komunikat o niepoprawnym symbolu
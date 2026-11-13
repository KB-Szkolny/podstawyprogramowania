###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12)'))  # Wypisuje komunikat proszący użytkownika o wpisanie numeru miesiąca, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej month

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :  # Sprawdza warunek: czy numer miesiąca (month) jest równy 1, 3, 5, 7, 8, 10 lub 12 (miesiące z 31 dniami)
    days = 31  # Jeśli warunek jest prawdziwy, przypisuje wartość 31 do zmiennej days (miesiące z 31 dniami)
elif month==2 :  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy numer miesiąca jest równy 2 (luty)
    days = 28  # Jeśli warunek jest prawdziwy, przypisuje wartość 28 do zmiennej days (luty ma 28 dni)
else:  # Jeśli żaden z powyższych warunków nie jest prawdziwy, czyli miesiąc ma 30 dni (4, 6, 9, 11)
    days = 30  # Przypisuje wartość 30 do zmiennej days

print(f'Month {month} has {days} days')  # Wypisuje numer miesiąca i liczbę dni w tym miesiącu
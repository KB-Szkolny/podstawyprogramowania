###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))  # Wypisuje komunikat proszący użytkownika o wpisanie numeru miesiąca, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej month
day = int(input('Enter the day number of the month: '))  # Wypisuje komunikat proszący użytkownika o wpisanie numeru dnia miesiąca, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej day
day_ok = False  # Przypisuje wartość False do zmiennej day_ok, która oznacza że dzień jest niepoprawny

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:  # Sprawdza warunek: czy numer miesiąca (month) jest równy 1, 3, 5, 7, 8, 10 lub 12 (miesiące z 31 dniami)
    if day >=1 and day <= 31:  # Jeśli warunek jest prawdziwy, sprawdza czy dzień (day) jest większy lub równy 1 ORAZ mniejszy lub równy 31
        day_ok = True  # Jeśli warunek jest prawdziwy, przypisuje wartość True do zmiennej day_ok, oznaczając że dzień jest poprawny
elif month== 2:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy numer miesiąca jest równy 2 (luty)
    if day >=1 and day <= 28:  # Jeśli warunek jest prawdziwy, sprawdza czy dzień (day) jest większy lub równy 1 ORAZ mniejszy lub równy 28
        day_ok = True  # Jeśli warunek jest prawdziwy, przypisuje wartość True do zmiennej day_ok, oznaczając że dzień jest poprawny
else:  # Jeśli żaden z powyższych warunków nie jest prawdziwy, czyli miesiąc ma 30 dni (4, 6, 9, 11)
    if day >=1 and day <= 30:  # Sprawdza czy dzień (day) jest większy lub równy 1 ORAZ mniejszy lub równy 30
        day_ok = True  # Jeśli warunek jest prawdziwy, przypisuje wartość True do zmiennej day_ok, oznaczając że dzień jest poprawny


message = (f'Day {day} for the month {month}')  # Tworzy komunikat z numerem dnia i numerem miesiąca i przypisuje do zmiennej message
if day_ok:  # Sprawdza warunek: czy zmienna day_ok ma wartość True
    print(f'{message} is correct')  # Jeśli warunek jest prawdziwy, wypisuje że dzień jest poprawny
else:  # Jeśli warunek jest fałszywy, czyli dzień jest niepoprawny
    print(f'{message} is not correct')  # Wypisuje że dzień jest niepoprawny
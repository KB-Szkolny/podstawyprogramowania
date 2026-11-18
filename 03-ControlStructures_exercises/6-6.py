hours = float(input("How many hours the car was parked?: "))  # Wypisuje komunikat proszący użytkownika o wpisanie liczby godzin parkowania, pobiera wpisany tekst, konwertuje go na liczbę zmiennoprzecinkową i przypisuje do zmiennej hours

if hours < 1:  # Sprawdza warunek: czy liczba godzin (hours) jest mniejsza niż 1
    print("No fee")  # Jeśli warunek jest prawdziwy, wypisuje komunikat o braku opłaty
elif hours >= 1 and hours < 3:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy liczba godzin jest większa lub równa 1 ORAZ mniejsza niż 3
    print("fee of 5PLN")  # Jeśli warunek jest prawdziwy, wypisuje opłatę w wysokości 5 PLN
elif hours >= 3 and hours < 7:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy liczba godzin jest większa lub równa 3 ORAZ mniejsza niż 7
    print("fee of 15PLN")  # Jeśli warunek jest prawdziwy, wypisuje opłatę w wysokości 15 PLN
elif hours > 6:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy liczba godzin jest większa niż 6
    print("fee of 20PLN")  # Jeśli warunek jest prawdziwy, wypisuje opłatę w wysokości 20 PLN
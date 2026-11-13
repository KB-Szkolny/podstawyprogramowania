###  # Nagłówek sekcji kodu
# Calculates and prints the quarter of the year for a given  # Nagłówek opisujący cel programu: oblicza i wypisuje kwartał roku dla podanego
# month number (1..12)  # numeru miesiąca (1..12)
#  # Pusta linia komentarza
month = int(input('Enter month number (1..12): '))  # Wypisuje komunikat proszący użytkownika o wpisanie numeru miesiąca, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej month

if month >= 10:  # Sprawdza warunek: czy numer miesiąca (month) jest większy lub równy 10
    quarter = 4  # Jeśli warunek jest prawdziwy, przypisuje wartość 4 do zmiennej quarter (czwarty kwartał)
elif month >= 7:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy numer miesiąca jest większy lub równy 7
    quarter = 3  # Jeśli warunek jest prawdziwy, przypisuje wartość 3 do zmiennej quarter (trzeci kwartał)
elif month >= 4:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy numer miesiąca jest większy lub równy 4
    quarter = 2  # Jeśli warunek jest prawdziwy, przypisuje wartość 2 do zmiennej quarter (drugi kwartał)
elif month >= 1:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy numer miesiąca jest większy lub równy 1
    quarter = 1  # Jeśli warunek jest prawdziwy, przypisuje wartość 1 do zmiennej quarter (pierwszy kwartał)
else:  # Jeśli żaden z powyższych warunków nie jest prawdziwy, czyli numer miesiąca jest niepoprawny
    print('Wrong month number!')  # Wypisuje komunikat o niepoprawnym numerze miesiąca

print(f'Month {month} is in quarter {quarter}')  # Wypisuje numer miesiąca i odpowiadający mu kwartał
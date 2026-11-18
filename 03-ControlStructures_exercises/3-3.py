###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))  # Wypisuje komunikat proszący użytkownika o wpisanie wieku, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej age

if age < 18 or age >= 65 :  # Sprawdza warunek: czy wiek (age) jest mniejszy niż 18 LUB większy lub równy 65
    print('You are eligible for a discount')  # Jeśli warunek jest prawdziwy, wypisuje że użytkownik ma prawo do rabatu
else:  # Jeśli warunek jest fałszywy, czyli wiek jest od 18 do 64 lat
    print('You are not eligible for a discount')  # Wypisuje że użytkownik nie ma prawa do rabatu
human_age = int(input("Dog's age in human years: "))  # Wypisuje komunikat proszący użytkownika o wpisanie wieku psa w latach ludzkich, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej human_age

if human_age <= 2:  # Sprawdza warunek: czy wiek psa w latach ludzkich (human_age) jest mniejszy lub równy 2
    dog_age = 10.5 * human_age  # Jeśli warunek jest prawdziwy, oblicza wiek psa w latach psich, mnożąc wiek ludzki przez 10.5
else:  # Jeśli warunek jest fałszywy, czyli wiek psa w latach ludzkich jest większy niż 2
    dog_age = 21 + (human_age - 2) * 4  # Oblicza wiek psa w latach psich, dodając 21 do iloczynu (wiek ludzki minus 2) razy 4

print(f"Dog's age in dog's years is {dog_age}")  # Wypisuje wiek psa w latach psich
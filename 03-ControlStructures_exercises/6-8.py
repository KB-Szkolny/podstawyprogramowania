###
# Checking if both people are adults
#
person1_name = input('Enter first person name: ')  # Wypisuje komunikat proszący użytkownika o wpisanie imienia pierwszej osoby i przypisuje wpisany tekst do zmiennej person1_name
person1_age = int(input('Enter first person age: '))  # Wypisuje komunikat proszący użytkownika o wpisanie wieku pierwszej osoby, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej person1_age
person2_name = input('Enter second person name: ')  # Wypisuje komunikat proszący użytkownika o wpisanie imienia drugiej osoby i przypisuje wpisany tekst do zmiennej person2_name
person2_age = int(input("Enter second person age: "))  # Wypisuje komunikat proszący użytkownika o wpisanie wieku drugiej osoby, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej person2_age
if person1_age >= 18 and person2_age  >= 18:  # Sprawdza warunek: czy wiek pierwszej osoby (person1_age) jest większy lub równy 18 ORAZ czy wiek drugiej osoby (person2_age) jest większy lub równy 18
    print(f'Both {person1_name} and {person2_name} are adults')  # Jeśli warunek jest prawdziwy, wypisuje że obie osoby są pełnoletnie
else:  # Jeśli warunek jest fałszywy, czyli przynajmniej jedna osoba nie jest pełnoletnia
    print(f'Either {person1_name} or {person2_name} is not an adult')  # Wypisuje że jedna z osób nie jest pełnoletnia
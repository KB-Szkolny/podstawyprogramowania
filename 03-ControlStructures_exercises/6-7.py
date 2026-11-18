user_age = int(input("How old are you? : "))  # Wypisuje komunikat proszący użytkownika o wpisanie wieku, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej user_age

if user_age < 13:  # Sprawdza warunek: czy wiek użytkownika (user_age) jest mniejszy niż 13
    print("Your age group: Child")  # Jeśli warunek jest prawdziwy, wypisuje grupę wiekową: Dziecko
elif user_age >= 13 and user_age <= 19:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy wiek jest większy lub równy 13 ORAZ mniejszy lub równy 19
    print("Your age group: Teen")  # Jeśli warunek jest prawdziwy, wypisuje grupę wiekową: Nastolatek
elif user_age >= 20 and user_age <= 64:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy wiek jest większy lub równy 20 ORAZ mniejszy lub równy 64
    print("Your age group: Adult")  # Jeśli warunek jest prawdziwy, wypisuje grupę wiekową: Dorosły
elif user_age >= 65:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy wiek jest większy lub równy 65
    print("Your age group: Senior")  # Jeśli warunek jest prawdziwy, wypisuje grupę wiekową: Senior
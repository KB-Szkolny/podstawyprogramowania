# Program oblicza i wyświetla łączną liczbę godzin wszystkich przedmiotów
# zapisanych w słowniku winter_semester.

def main():
    # Słownik przechowujący nazwy przedmiotów oraz liczbę przypisanych godzin
    winter_semester = {
        "math": 60,
        "programming": 30,
        "history": 15
    }

    # Metoda .values() zwraca wszystkie liczby godzin, a sum() oblicza ich łączną sumę
    total_hours = sum(winter_semester.values())

    print(f"The total number of hours in the winter semester is {total_hours}")

if __name__ == "__main__":
    main()
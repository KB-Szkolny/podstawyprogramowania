def f(password):                        # Definicja funkcji sprawdzającej poprawność hasła
    if len(password) < 6:               # Sprawdzenie, czy hasło ma mniej niż 6 znaków
        return False                    # Jeśli jest za krótkie, od razu zwracamy False

    return len(set(password)) == len(password)  # Zbiór set() usuwa duplikaty; jeśli długość się nie zmieniła, znaki są unikalne

def main():                             # Główna funkcja testująca
    print(f("ax15"))                    # Za krótkie (4 znaki) -> False
    print(f("book123"))                 # Powtarza się litera 'o' -> False
    print(f("A2water3"))                # Min. 6 znaków i brak powtórzeń -> True
    print(f("qwerty"))                  # Dokładnie 6 unikalnych znaków -> True
    print(f(""))                        # Puste hasło -> False

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
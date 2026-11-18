import range_check                      # Import własnego modułu range_check.py

def main():                             # Główna funkcja programu
    x = 2                               # Dolna granica przedziału
    y = 15                              # Górna granica przedziału
    number = int(input("A number: "))   # Pobranie liczby od użytkownika i zamiana na int

    if range_check.is_in_range(number, x, y):   # Sprawdzenie przedziału funkcją z modułu
        result = "yes"                  # Jeśli funkcja zwróciła True
    else:
        result = "no"                   # Jeśli funkcja zwróciła False

    print(f"Number {number} in the range <{x},{y}>: {result}")  # Wyświetlenie wyniku

if __name__ == "__main__":              # Punkt startowy programu
    main()
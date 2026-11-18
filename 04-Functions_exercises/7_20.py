def is_prime(num):                      # Pomocnicza funkcja sprawdzająca, czy liczba jest pierwsza
    if num < 2:                         # Liczby mniejsze niż 2 nie są pierwsze
        return False
    for i in range(2, int(num ** 0.5) + 1): # Sprawdzamy dzielniki od 2 do pierwiastka z liczby
        if num % i == 0:                # Jeśli znajdzie się dzielnik bez reszty
            return False                # Liczba nie jest pierwsza
    return True                         # Brak dzielników oznacza, że liczba jest pierwsza

def f(n):                               # Definicja funkcji zwracającej n-tą liczbę pierwszą
    count = 0                           # Licznik znalezionych dotychczas liczb pierwszych
    candidate = 1                       # Aktualnie sprawdzana liczba

    while count < n:                    # Szukamy tak długo, aż znajdziemy n liczb pierwszych
        candidate += 1                  # Przechodzimy do kolejnej liczby naturalnej
        if is_prime(candidate):         # Jeśli liczba jest pierwsza
            count += 1                  # Zwiększamy licznik znalezionych liczb pierwszych

    return candidate                    # Zwracamy n-tą znalezioną liczbę pierwszą

def main():                             # Główna funkcja testująca
    print(f(1))                         # 1. liczba pierwsza -> 2
    print(f(5))                         # 5. liczba pierwsza (2, 3, 5, 7, 11) -> 11

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
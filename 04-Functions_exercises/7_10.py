def f(x, y):                            # Definicja funkcji zliczającej ujemne liczby parzyste w zakresie <x, y>
    count = 0                           # Licznik pasujących liczb (na start 0)

    for i in range(x, y + 1):           # Pętla przechodząca przez wszystkie liczby całkowite od x do y włącznie
        if i < 0 and i % 2 == 0:        # Sprawdzenie, czy liczba jest ujemna (< 0) oraz parzysta (% 2 == 0)
            count += 1                  # Zwiększenie licznika o 1

    return count                        # Zwrócenie liczby znalezionych wartości

def main():                             # Główna funkcja testująca
    print(f(-7, 8))                     # Pasujące liczby: -6, -4, -2 -> 3
    print(f(-1, 11))                    # Brak ujemnych liczb parzystych -> 0

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
def f(number, even):                    # Definicja funkcji sumującej cyfry parzyste lub nieparzyste
    total = 0                           # Zmienna przechowująca sumę wybranych cyfr

    for ch in str(number):              # Zamiana liczby na tekst i przejście przez każdą jej cyfrę
        digit = int(ch)                 # Zamiana pojedynczego znaku z powrotem na liczbę całkowitą
        if even and digit % 2 == 0:     # Jeśli even == True i cyfra jest parzysta
            total += digit              # Dodajemy cyfrę parzystą do sumy
        elif not even and digit % 2 != 0:   # Jeśli even == False i cyfra jest nieparzysta
            total += digit              # Dodajemy cyfrę nieparzystą do sumy

    return total                        # Zwrócenie obliczonej sumy

def main():                             # Główna funkcja testująca
    print(f(3124, True))                # 2 + 4 = 6
    print(f(3124, False))               # 3 + 1 = 4
    print(f(20576, False))              # 5 + 7 = 12
    print(f(20576, True))               # 2 + 0 + 6 = 8
    print(f(13115, True))               # Brak cyfr parzystych -> 0

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
def f(x, y):                            # Definicja funkcji sumującej liczby z przedziału <x, y>
    total = 0                           # Zmienna przechowująca sumę pasujących liczb

    for i in range(x, y + 1):           # Pętla przechodząca przez wszystkie liczby od x do y włącznie
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:    # Podzielna przez 2 i 3, ale nie przez 4
            total += i                  # Dodanie liczby spełniającej warunki do sumy

    return total                        # Zwrócenie obliczonej sumy

def main():                             # Główna funkcja testująca
    print(f(1, 20))                     # 6 + 18 = 24 (12 odpada, bo dzieli się przez 4)
    print(f(10, 30))                    # 18 + 30 = 48 (12 i 24 odpadają, bo dzielą się przez 4)

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
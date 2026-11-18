def f(amount_to_pay):                   # Definicja funkcji obliczającej minimalną liczbę monet
    coins_5 = amount_to_pay // 5        # Liczba monet 5 PLN (dzielenie całkowite)
    remainder = amount_to_pay % 5       # Reszta kwoty do zapłaty po użyciu piątek

    coins_2 = remainder // 2            # Liczba monet 2 PLN z pozostałej kwoty
    coins_1 = remainder % 2             # Reszta (0 lub 1) to liczba monet 1 PLN

    return coins_5 + coins_2 + coins_1  # Zwrócenie łącznej minimalnej liczby monet

def main():                             # Główna funkcja testująca
    print(f(23))                        # 4x5 + 1x2 + 1x1 -> 6
    print(f(8))                         # 1x5 + 1x2 + 1x1 -> 3
    print(f(2))                         # 0x5 + 1x2 + 0x1 -> 1
    print(f(0))                         # 0 monet -> 0

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
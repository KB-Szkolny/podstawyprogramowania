def f(product_code):                 # Definicja funkcji sprawdzającej poprawność kodu produktu
    d1 = int(product_code[0])       # Pierwsza cyfra kodu zamieniona na liczbę całkowitą
    d2 = int(product_code[1])       # Druga cyfra kodu
    d3 = int(product_code[2])           # Trzecia cyfra kodu
    control_digit = int(product_code[3])# Czwarta cyfra (kontrolna)

    remainder = (d1 + d2 + d3) % 7      # Reszta z dzielenia sumy pierwszych trzech cyfr przez 7
    return remainder == control_digit   # Zwraca True, jeśli reszta zgadza się z cyfrą kontrolną, inaczej False

def main():        # Główna funkcja testująca
    print(f("1082"))    # (1 + 0 + 8) % 7 = 2 -> True
    print(f("2035"))         # (2 + 0 + 3) % 7 = 5 -> True
    print(f("1114"))          # (1 + 1 + 1) % 7 = 3 != 4 -> False
    print(f("7071"))          # (7 + 0 + 7) % 7 = 0 != 1 -> False

if __name__ == "__main__":     # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
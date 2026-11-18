def f(n):                  # Definicja funkcji zwracającej n-ty wyraz ciągu Fibonacciego
    if n == 1:               # Pierwszy wyraz ciągu (indeksowany od 1) to 0
        return 0
    elif n == 2:           # Drugi wyraz ciągu to 1
        return 1

    a, b = 0, 1                   # Dwa pierwsze wyrazy ciągu (n=1 oraz n=2)
    for _ in range(3, n + 1):      # Obliczamy kolejne wyrazy od 3. do n-tego
        a, b = b, a + b            # Przesunięcie: nowy wyraz to suma dwóch poprzednich

    return b                   # Zwrócenie n-tego wyrazu ciągu

def main():                    # Główna funkcja testująca
    print(f(5))                  # Ciąg: 0, 1, 1, 2, 3 -> 3
    print(f(9))                  # Ciąg: 0, 1, 1, 2, 3, 5, 8, 13, 21 -> 21

if __name__ == "__main__":     # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
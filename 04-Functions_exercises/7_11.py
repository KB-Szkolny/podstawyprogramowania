def f(n1, n2, n3):                      # Definicja funkcji sprawdzającej, czy chociaż jedna liczba jest ujemna
    return n1 < 0 or n2 < 0 or n3 < 0   # Zwraca True, jeśli którakolwiek z liczb jest mniejsza od 0, inaczej False

def main():                             # Główna funkcja testująca
    print(f(11, 6, -4))                 # -4 < 0 -> True
    print(f(5, 4, 14))                  # Żadna nie jest ujemna -> False

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
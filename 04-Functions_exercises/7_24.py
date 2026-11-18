def f(expression):                    # Definicja funkcji obliczającej wartość wyrażenia
    total = int(expression[0])          # Pierwsza cyfra z lewej strony jako wartość startowa

    for i in range(1, len(expression), 2):  # Przeskakujemy co 2 znaki, trafiając na same operatory (+ lub -)
        operator = expression[i]        # Odczytanie znaku działania (+ lub -)
        number = int(expression[i + 1]) # Odczytanie kolejnej cyfry stojącej tuż po operatorze

        if operator == "+":             # Jeśli operatorem jest plus
            total += number             # Dodajemy cyfrę do wyniku
        elif operator == "-":           # Jeśli operatorem jest minus
            total -= number             # Odejmujemy cyfrę od wyniku

    return total                        # Zwrócenie końcowej wartości wyrażenia

def main():                             # Główna funkcja testująca
    print(f("2+3"))                     # Wynik: 5
    print(f("3+8+1"))                   # Wynik: 12
    print(f("2+3-4+5-0"))               # Wynik: 6

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
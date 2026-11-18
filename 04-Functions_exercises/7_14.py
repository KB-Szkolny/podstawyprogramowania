def f(number1, number2, operator):      # Definicja funkcji wykonującej wybrane działanie arytmetyczne
    if operator == "+":                 # Dodawanie
        return number1 + number2
    elif operator == "-":               # Odejmowanie
        return number1 - number2
    elif operator == "*":               # Mnożenie
        return number1 * number2
    elif operator == "%":               # Reszta z dzielenia (modulo)
        return number1 % number2
    elif operator == "**":              # Potęgowanie
        return number1 ** number2

def main():                             # Główna funkcja testująca
    print(f(2, 3, "+"))                 # Wynik: 5
    print(f(2, 3, "%"))                 # Wynik: 2
    print(f(2, 3, "**"))                # Wynik: 8
    print(f(2, 3, "*"))                 # Wynik: 6
    print(f(2, 3, "-"))                 # Wynik: -1

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
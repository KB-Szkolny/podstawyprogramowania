def f(number1, number2, number3):       # Definicja funkcji przyjmującej trzy liczby
    largest = max(number1, number2, number3)    # Wyznaczenie największej z trzech liczb
    smallest = min(number1, number2, number3)   # Wyznaczenie najmniejszej z trzech liczb
    return largest - smallest           # Zwrócenie różnicy między największą a najmniejszą liczbą

def main():                             # Główna funkcja testująca
    print(f(7, 4, 9))                   # 9 - 4 = 5
    print(f(2, 12, 8))                  # 12 - 2 = 10

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
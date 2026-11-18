def f(n):                               # Definicja funkcji zwracającej n gwiazdek oddzielonych ukośnikiem
    return "/".join("*" * n)            # Tworzy napis z n gwiazdek ("*" * n) i łączy je znakiem "/"

def main():                             # Główna funkcja testująca
    print(f(4))                         # Wynik: */*/*/*
    print(f(1))                         # Wynik: *

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
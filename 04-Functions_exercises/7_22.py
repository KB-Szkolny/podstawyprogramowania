def f(name):                            # Definicja funkcji tworzącej akronim z podanego tekstu
    words = name.split()                # Podzielenie tekstu po spacjach na listę pojedynczych słów
    acronym = ""                        # Zmienna na wynikowy akronim (na start pusty napis)

    for word in words:                  # Pętla przechodząca przez każde słowo na liście
        acronym += word[0]              # Doklejenie pierwszej litery aktualnego słowa

    return acronym                      # Zwrócenie gotowego akronimu

def main():                             # Główna funkcja testująca
    print(f("Internet of Things"))      # Wynik: IoT
    print(f("For Your Information"))    # Wynik: FYI
    print(f("Python"))                  # Wynik: P

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
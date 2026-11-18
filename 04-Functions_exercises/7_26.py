def f(text):                            # Definicja funkcji łączącej znaki tekstu myślnikiem
    return "-".join(text)               # Metoda join() wstawia "-" pomiędzy każdy kolejny znak napisu

def main():                             # Główna funkcja testująca działanie programu
    print(f("University"))              # Wynik: U-n-i-v-e-r-s-i-t-y
    print(f("UE"))                      # Wynik: U-E
    print(f("x"))                       # Wynik: x (dla 1 znaku nie dodaje myślnika)
    print(f(""))                        # Wynik: "" (pusty tekst pozostaje pusty)

if __name__ == "__main__":              # Uruchomienie main() tylko przy bezpośrednim odpaleniu pliku
    main()
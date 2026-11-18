def f(binary_number):                   # Definicja funkcji sprawdzającej poprawność liczby binarnej
    for ch in binary_number:            # Pętla przechodząca przez każdy znak w napisie
        if ch not in ("0", "1"):        # Jeśli znak nie jest ani '0', ani '1'
            return False                # Od razu zwracamy False

    return len(binary_number) > 0       # Zwraca True, jeśli wszystkie znaki były poprawne (i napis nie był pusty)

def main():                             # Główna funkcja testująca
    print(f("101101"))                  # Same zera i jedynki -> True
    print(f("1311a10100"))              # Zawiera '3' oraz 'a' -> False

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
def f(number):                          # Definicja funkcji sumującej powtarzające się cyfry w liczbie
    digits = str(number)                # Zamiana liczby na tekst, aby móc zliczać jej cyfry
    total = 0                           # Zmienna przechowująca sumę powtarzających się cyfr

    for ch in digits:                   # Pętla przechodząca przez każdą cyfrę w liczbie
        if digits.count(ch) > 1:        # Jeśli dana cyfra występuje w liczbie więcej niż raz
            total += int(ch)            # Dodajemy jej wartość do sumy

    return total                        # Zwrócenie obliczonej sumy

def main():                             # Główna funkcja testująca
    print(f(1027))                      # Brak powtórzeń -> 0
    print(f(230335))                    # Cyfra 3 występuje 3 razy: 3 + 3 + 3 = 9
    print(f(513553007))                 # 5 (3 razy: 15) + 3 (2 razy: 6) + 0 (2 razy: 0) = 21

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
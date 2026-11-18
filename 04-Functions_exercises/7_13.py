def f(n):                               # Definicja funkcji łączącej liczby od 1 do n w jeden napis
    result = ""                         # Pusty napis na start, do którego będziemy doklejać liczby

    for i in range(1, n + 1):           # Pętla przechodząca po kolejnych liczbach od 1 do n włącznie
        result += str(i)                # Zamiana aktualnej liczby na tekst (str) i doklejenie do wyniku

    return result                       # Zwrócenie gotowego ciągu znaków

def main():                             # Główna funkcja testująca
    print(f(11))                        # Wynik: "1234567891011"
    print(f(4))                         # Wynik: "1234"

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
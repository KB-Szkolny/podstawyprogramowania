def f(sentence):              # Definicja funkcji usuwającej spacje ze zdania
    return sentence.replace(" ", "")   # Metoda replace() zamienia każdą spację na pusty ciąg znaków

def main():                        # Główna funkcja testująca
    print(f("integrated development environment"))
    print(f("A programming language is a system of notation for writing computer programs"))

if __name__ == "__main__":           # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
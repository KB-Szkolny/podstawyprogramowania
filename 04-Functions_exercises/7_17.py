def f(palindrome):                      # Definicja funkcji sprawdzającej
    return palindrome == palindrome[::-1]   # Porównuje oryginalny napis z jego odwróconą wersją 

def main():                    # Główna funkcja testująca
    print(f("radar"))          # "radar" == "radar" -> True
    print(f("12-11-21"))      # "12-11-21" == "12-11-21" -> True
    print(f("book"))          # "book" != "koob" -> False

if __name__ == "__main__":    # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
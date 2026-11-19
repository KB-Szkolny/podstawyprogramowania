# Program dzieli podany tekst na pojedyncze słowa i zlicza, ile razy każde z nich
# wystąpiło, zapisując wyniki w słowniku.

def main():
    paragraph = "cat dog mouse cat rat cat mouse"

    # Metoda .split() dzieli tekst po spacjach na listę pojedynczych słów
    words = paragraph.split()
    word_count = {}                             # Pusty słownik na wyniki (słowo -> liczba wystąpień)

    for word in words:
        if word in word_count:
            word_count[word] += 1               # Jeśli słowo już jest w słowniku, zwiększa licznik o 1
        else:
            word_count[word] = 1                # Jeśli słowo pojawia się pierwszy raz, ustawia licznik na 1

    # Wyświetlenie podsumowania dla każdego unikalnego słowa
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
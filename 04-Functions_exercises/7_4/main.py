import letter_counter                   # Import własnego modułu letter_counter.py

def main():                             # Główna funkcja programu
    text = "You never get a second chance to make a first impression"   # Badany tekst
    letter = "e"                        # Szukana litera
    count = letter_counter.count_letter(text, letter)   # Wywołanie funkcji z modułu

    print(text)                         # Wyświetlenie tekstu
    print(f"The number of letter '{letter}': {count}")  # Wyświetlenie liczby wystąpień litery

if __name__ == "__main__":              # Punkt startowy programu
    main()
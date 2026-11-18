def hide(card_number):                  # Definicja funkcji maskującej numer karty kredytowej
    first_two = card_number[:2]         # Pobranie pierwszych dwóch cyfr (indeksy 0 i 1)
    last_four = card_number[-4:]        # Pobranie ostatnich czterech cyfr od końca
    masked_middle = "*" * 10            # Środkowe 10 cyfr zastąpione gwiazdkami (16 - 2 - 4 = 10)
    return first_two + masked_middle + last_four    # Złączenie w jeden zamaskowany napis

if __name__ == "__main__":              # Kod testowy wykona się tylko przy bezpośrednim uruchomieniu card.py
    print(hide("5290312400019022"))     # Wynik testu: 52**********9022
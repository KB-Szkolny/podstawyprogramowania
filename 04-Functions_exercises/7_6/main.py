import card                             # Import własnego modułu card.py

def main():                             # Główna funkcja programu
    card_num = "5290312400019022"       # Przykładowy 16-cyfrowy numer karty
    masked_card = card.hide(card_num)   # Wywołanie funkcji hide() z modułu card
    print(masked_card)                  # Wyświetlenie zamaskowanego numeru karty

if __name__ == "__main__":              # Punkt startowy programu
    main()
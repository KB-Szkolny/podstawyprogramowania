#Program tłumaczy angielskie słowo wpisane przez użytkownika na język polski
# na podstawie słownika translations lub informuje o braku tłumaczenia.
def main():
    # Słownik mapujący angielskie słowa (klucze) na polskie tłumaczenia (wartości)
    translations = {
        'computer': 'komputer',
        'mouse': 'myszka',
        'keyboard': 'klawiatura',
        'printer': 'drukarka'
    }

    # Pobranie słowa od użytkownika i sprowadzenie do małych liter (.strip().lower())
    word = input("Enter an English word: ").strip().lower()

    # Sprawdzenie, czy podane słowo istnieje jako klucz w słowniku
    if word in translations:
        print(f"Polish translation: {translations[word]}")
    else:
        print("Translation is unavailable.")

if __name__ == "__main__":
    main()
# Program wczytuje z pliku euro.json 10 ostatnich notowań kursu Euro (tabela C z NBP)
# i wyświetla datę, kurs kupna oraz kurs sprzedaży w czytelnej tabeli.

import json

def main():
    # Wczytanie danych z pliku euro.json pobranego wcześniej z API NBP
    with open('09-DictionariesStacksAndQueues_exercises/euro.json', 'r', encoding='utf-8') as file:
        data = json.load(file)                  # Główny obiekt JSON z danymi waluty EUR

    # Wyświetlenie nagłówka tabeli wyrównanego do szerokości 16 znaków na kolumnę (<16)
    print(f"{'Date':<16}{'Buying Rate':<16}{'Selling Rate'}")
    print("=" * 44)

    # Lista 10 notowań znajduje się pod kluczem 'rates' – każde notowanie to osobny słownik
    for rate in data["rates"]:
        date = rate["effectiveDate"]            # Data publikacji danego notowania
        buying = rate["bid"]                    # Kurs kupna waluty (bid)
        selling = rate["ask"]                   # Kurs sprzedaży waluty (ask)
        print(f"{date:<16}{buying:<16.4f}{selling:.4f}")   # .4f formatuje kurs do 4 miejsc po przecinku

if __name__ == "__main__":
    main()
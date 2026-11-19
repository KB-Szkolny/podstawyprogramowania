def main():                                                         # Główna funkcja programu
    countries = [                                                   # Lista składająca się z 5 słowników
        {"name": "Poland", "population": 38000000},                 # Słownik 1: Polska
        {"name": "Germany", "population": 83000000},                # Słownik 2: Niemcy
        {"name": "France", "population": 68000000},                 # Słownik 3: Francja
        {"name": "Spain", "population": 47000000},                  # Słownik 4: Hiszpania
        {"name": "Italy", "population": 59000000}                   # Słownik 5: Włochy
    ]

    print(f"{'COUNTRY':<10} {'POPULATION'}")                        # Nagłówek tabeli wyrównany do kolumn

    for country in countries:                                       # Pętla po każdym słowniku na liście
        print(f"{country['name']:<10} {country['population']}")     # Wypisanie nazwy kraju i populacji

if __name__ == "__main__":                                          # Punkt startowy programu
    main()                                                          # Wywołanie głównej funkcji
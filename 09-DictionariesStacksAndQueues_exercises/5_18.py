# Program wczytuje dane o psach z pliku dogs.json
# i wyświetla informacje tylko o tych psach, które mają mniej niż 5 lat.

import json

def main():
    # Odczyt listy słowników z pliku dogs.json
    with open('09-DictionariesStacksAndQueues_exercises/dogs.json', 'r', encoding='utf-8') as file:
        dogs = json.load(file)                  # Każdy element listy 'dogs' to słownik opisujący jednego psa

    # Przegląd wszystkich psów i filtrowanie po kluczu 'age'
    for dog in dogs:
        if dog["age"] < 5:                      # Sprawdza, czy wiek psa jest mniejszy niż 5 lat
            for key, value in dog.items():      # Wypisuje wszystkie dane pasującego psa
                print(f"{key}: {value}")
            print()                             # Oddziela kolejny wpis pustą linią

if __name__ == "__main__":
    main()
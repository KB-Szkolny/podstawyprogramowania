# Program wczytuje pojedynczy słownik z pliku computer.json
# i wypisuje wszystkie jego parametry w formacie klucz : wartość.

import json

def main():
    # Otwarcie pliku JSON w trybie do odczytu ('r') z kodowaniem UTF-8
    with open('09-DictionariesStacksAndQueues_exercises/computer.json', 'r', encoding='utf-8') as file:
        data = json.load(file)                  # Parsuje zawartość pliku JSON do słownika Pythona

    # Iteracja po wszystkich parach klucz-wartość słownika i wyświetlenie ich w konsoli
    for key, value in data.items():
        print(key, ':', value)                  # Wypisuje nazwę parametru oraz jego wartość

if __name__ == "__main__":
    main()
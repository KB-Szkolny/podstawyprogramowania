# Program wczytuje listę słowników z pliku cities.json
# i wyświetla szczegółowe informacje o każdym mieście oddzielone pustą linią.

import json

def main():
    # Parametr encoding='utf-8' gwarantuje poprawne wyświetlenie polskich znaków (np. Kraków, Łódź)
    with open('09-DictionariesStacksAndQueues_exercises/cities.json', 'r', encoding='utf-8') as file:
        data = json.load(file)                  # Wczytuje tablicę obiektów JSON jako listę słowników

    # Zewnętrzna pętla przechodzi po kolejnych miastach na liście
    for city in data:
        # Wewnętrzna pętla wypisuje wszystkie pary (klucz, wartość) dla bieżącego miasta
        for key, value in city.items():
            print(key, ':', value)
        print()                                 # Pusta linia oddzielająca informacje o kolejnym mieście

if __name__ == "__main__":
    main()
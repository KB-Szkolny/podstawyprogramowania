# Program wczytuje z pliku province.csv przypisanie pierwszych liter tablic rejestracyjnych
# do województw, a następnie zlicza, ile pojazdów z pliku vehicle.txt pochodzi z każdego z nich.

import csv  # Moduł ułatwiający odczyt danych rozdzielonych przecinkami z pliku CSV

def main():
    provinces = {}      # Słownik mapujący literę na nazwę województwa (np. 'K' -> 'Małopolskie')
    vehicle_counts = {} # Słownik zliczający pojazdy dla każdego województwa (np. 'Małopolskie' -> 0)

    # 1. Wczytanie słownika województw z pliku province.csv
    with open('09-DictionariesStacksAndQueues_exercises/province.csv', encoding='utf-8') as file:
        reader = csv.reader(file)               # Dzieli każdy wiersz po przecinku na dwie wartości: literę i nazwę
        next(reader)                            # Pomija pierwszy wiersz z nagłówkami kolumn (Letter,Name)
        for letter, name in reader:
            provinces[letter] = name            # Zapisuje parę (litera -> województwo) w słowniku provinces
            vehicle_counts[name] = 0            # Tworzy licznik dla tego województwa ustawiony na 0

    # 2. Odczyt numerów rejestracyjnych z pliku vehicle.txt i zliczanie pojazdów
    with open('09-DictionariesStacksAndQueues_exercises/vehicle.txt', encoding='utf-8') as file:
        for line in file:
            first_letter = line.strip()[0]      # Usuwa znak nowej linii i pobiera pierwszą literę rejestracji
            province = provinces[first_letter]  # Odszukuje nazwę województwa na podstawie pierwszej litery
            vehicle_counts[province] += 1       # Zwiększa licznik pojazdów dla tego województwa o 1

    # 3. Wyświetlenie końcowego zestawienia dla wszystkich województw
    for province, count in vehicle_counts.items():
        print(f"{province}: {count}")

if __name__ == "__main__":
    main()
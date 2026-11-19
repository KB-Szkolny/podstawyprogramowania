# Program odczytuje dotychczasowe wyniki głosowania z pliku voting.json,
# zwiększa liczbę głosów wybranej osoby o 1 (lub dodaje ją z wynikiem 1) i zapisuje zmiany.

import json
import os

def main():
    file_path = '09-DictionariesStacksAndQueues_exercises/voting.json'

    # 1. Sprawdzenie, czy plik istnieje – jeśli tak, wczytujemy dotychczasowe głosy jako słownik
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            votes = json.load(file)
    else:
        votes = {}                              # Jeśli plik jeszcze nie istnieje, zaczynamy z pustym słownikiem

    # 2. Pobranie imienia kandydata i aktualizacja licznika głosów
    person_name = input('Name of the person you are voting for: ').strip()
    if person_name in votes:
        votes[person_name] += 1                 # Zwiększa liczbę głosów istniejącej osoby
    else:
        votes[person_name] = 1                  # Dodaje nową osobę z 1 głosem na start

    # 3. Zapis zaktualizowanego słownika z powrotem do pliku JSON (ensure_ascii=False zachowuje polskie znaki)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(votes, file, indent=4, ensure_ascii=False)

    print("Updated voting results:", votes)

if __name__ == "__main__":
    main()
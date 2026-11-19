# Program tworzy słownik opisujący ulubiony film (min. 5 par klucz-wartość)
# i zapisuje go do pliku favourite.json.

import json

def main():
    # Słownik zawierający 5 par klucz-wartość różnych typów (str, int, list, float)
    favourite_movie = {
        "title": "Inception",                   # Tytuł filmu (str)
        "director": "Christopher Nolan",        # Reżyser (str)
        "release_year": 2010,                   # Rok premiery (int)
        "genre": ["Sci-Fi", "Action", "Thriller"],  # Lista gatunków (list)
        "rating": 8.8                           # Ocena (float)
    }

    file_name = "09-DictionariesStacksAndQueues_exercises/favourite.json"

    # Zapis słownika do pliku JSON w czytelnym formacie z wcięciami na 4 spacje
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(favourite_movie, file, indent=4, ensure_ascii=False)

    print("Favourite movie data has been saved to", file_name)

if __name__ == "__main__":
    main()
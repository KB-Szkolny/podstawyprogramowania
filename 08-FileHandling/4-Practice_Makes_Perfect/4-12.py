# Zadanie 4-12
# Plik books.csv zawiera dane o książkach.
books_file = "books.csv"
genre_files = {
    "Fantasy": "books_fantasy.txt",
    "Historical": "books_historical.txt",
    "Romance": "books_romance.txt",
    "Classic": "books_classic.txt",
}


def copy_genre(genre: str) -> str:
    """Zapisuje wiersze książek wybranego gatunku do przypisanego pliku."""
    # Nazwa pliku zależy od wybranego gatunku.
    output_file = genre_files[genre]
    # Książki są odczytywane z CSV, a wybrane rekordy trafiają do nowego pliku.
    with open(books_file, "r", encoding="utf-8", newline="") as source:
        with open(output_file, "w", encoding="utf-8", newline="") as destination:
            # Nagłówek i układ kolumn pozostają takie jak w pliku źródłowym.
            reader = csv.DictReader(source)
            writer = csv.DictWriter(destination, fieldnames=reader.fieldnames)
            writer.writeheader()
            for book in reader:
                # Do pliku trafiają tylko książki wybranego gatunku.
                if book["Genre"] == genre:
                    writer.writerow(book)
    # Funkcja zwraca nazwę pliku do wyświetlenia po zakończeniu.
    return output_file


# Użytkownik podaje gatunek, który ma zostać skopiowany.
selected_genre = input(
    "Enter genre (Fantasy, Historical, Romance, Classic): "
).strip()
# Nieznany gatunek powoduje komunikat zamiast utworzenia pliku.
if selected_genre not in genre_files:
    print("Unknown genre. No file was created.")
else:
    # Pasujące książki są kopiowane, a nazwa utworzonego pliku jest wyświetlana.
    result_file = copy_genre(selected_genre)
    print(f"Books saved to {result_file}.")

# Zadanie 4-6
def file_statistics(file_name: str) -> tuple:
    """Zwraca liczbę wierszy, znaków i słów w pliku tekstowym."""
    # Przyjmujemy samą nazwę pliku, żeby odczyt pozostał w folderze projektu.
    if any(separator in file_name for separator in ("/", "\\", ":")):
        raise ValueError("Enter a file name without a folder path.")

    # Odczytaj plik wskazany przez użytkownika.
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    # Wynikiem są liczby wierszy, znaków i słów.
    return len(content.splitlines()), len(content), len(content.split())


# Nazwa pliku pochodzi od użytkownika.
file_name = input("File name: ").strip()
try:
    line_count, character_count, word_count = file_statistics(file_name)
except FileNotFoundError:
    print(f"Error: file not found: {file_name}")
except IsADirectoryError:
    print(f"Error: not a text file: {file_name}")
except UnicodeDecodeError:
    print(f"Error: file is not encoded as UTF-8: {file_name}")
except ValueError as error:
    print(f"Error: {error}")
else:
    # Wyniki są wyświetlane po poprawnym odczytaniu pliku.
    print("Number of lines:", line_count)
    print("Number of characters:", character_count)
    print("Number of words:", word_count)

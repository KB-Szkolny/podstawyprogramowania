# Zadanie 4-8
# Plik files.txt zawiera nazwy do sprawdzenia.
files_list = "files.txt"
import re  # import modułu do wyrażeń regularnych
# Wzorzec pasuje do nazw z rozszerzeniem mającym dokładnie cztery znaki.
four_character_extension = re.compile(r"\.[^.]{4}$")

# Każda nazwa z pliku jest sprawdzana osobno.
with open(files_list, "r", encoding="utf-8") as file:
    for line in file:
        # Zmienna file_name nie zawiera już znaku końca wiersza.
        file_name = line.strip()
        # Nazwa jest wypisywana, gdy jej rozszerzenie ma cztery znaki.
        if four_character_extension.search(file_name):
            print(file_name)

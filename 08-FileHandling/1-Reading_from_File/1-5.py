# Zadanie 1-5
# Plik countries.txt jest odczytywany z folderu projektu.
countries_file = "countries.txt"

# Skrypt odczytuje kraje i wypisuje je z numerami.
with open(countries_file, "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        # Końcowy znak nowej linii znika, żeby numer i kraj były obok siebie.
        print(f"{number}. {line.rstrip()}")

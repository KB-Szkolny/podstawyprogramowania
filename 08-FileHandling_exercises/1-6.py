# Zadanie 1-6
# Plik countries.txt jest odczytywany z folderu projektu.
countries_file = "countries.txt"

# Nazwy krajów trafiają do listy bez końcowych znaków nowej linii.
with open(countries_file, "r", encoding="utf-8") as file:
    countries = file.read().splitlines()

# Pętla wypisuje kraje alfabetycznie.
for country in sorted(countries):
    print(country)

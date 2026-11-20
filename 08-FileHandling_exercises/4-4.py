# Zadanie 4-4
# Lista pracowników znajduje się w pliku it_company.csv.
employees_file = "it_company.csv"
batch_size = 5

# Program wczytuje zawartość pliku wraz z nagłówkiem.
with open(employees_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Kolejne porcje zawierają po pięć wierszy.
for start in range(0, len(lines), batch_size):
    # Ostatnia porcja zawiera mniej wierszy, jeśli plik nie dzieli się równo przez pięć.
    batch = lines[start : start + batch_size]
    for line in batch:
        print(line, end="")

    # Program czeka na Enter tylko wtedy, gdy zostały jeszcze wiersze do pokazania.
    if start + batch_size < len(lines):
        input("\nPress Enter key...")

# Zadanie 2-3
# Plik źródłowy i jego kopia znajdują się w folderze projektu.
original_file = "healthy_lifestyle.txt"
copy_file = "copy_healthy_lifestyle.txt"

# Program najpierw odczytuje całą treść oryginału.
with open(original_file, "r", encoding="utf-8") as source:
    content = source.read()

# Ta sama treść jest zapisywana w nowym pliku.
with open(copy_file, "w", encoding="utf-8") as destination:
    destination.write(content)

# Komunikat potwierdza utworzenie kopii.
print(f"Copied {original_file} to {copy_file}.")

# Zadanie 4-11
# Wyniki są zapisywane w pliku powers.txt w folderze projektu.
powers_file = "powers.txt"

# Plik jest tworzony lub jego poprzednia zawartość jest zastępowana.
with open(powers_file, "w", encoding="utf-8") as file:
    # Pętla obejmuje liczby od 1 do 100.
    for number in range(1, 101):
        # Wiersz zawiera liczbę, jej kwadrat i sześcian oddzielone przecinkami.
        row = f"{number},{number**2},{number**3}"
        # Wiersz jest wyświetlany i zapisywany w pliku.
        print(row)
        file.write(f"{row}\n")

# Komunikat potwierdza zakończenie zapisu.
print(f"Saved powers for 1-100 to {powers_file}.")

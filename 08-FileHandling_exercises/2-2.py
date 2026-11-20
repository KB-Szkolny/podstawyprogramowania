# Zadanie 2-2
# Plik seven_wonders.txt powstaje w folderze projektu.
output_file = "seven_wonders.txt"
seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal",
]

# Nazwy są zapisywane w kolejności alfabetycznej, każda w osobnej linii.
with open(output_file, "w", encoding="utf-8") as file:
    for wonder in sorted(seven_wonders):
        file.write(f"{wonder}\n")

# Komunikat potwierdza liczbę zapisanych nazw i miejsce zapisu.
print(f"Saved {len(seven_wonders)} wonders to {output_file}.")

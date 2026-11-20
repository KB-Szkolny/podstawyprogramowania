# Zadanie 1-8
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# Wbudowana funkcja sorted() sortuje listę alfabetycznie bez zmiany oryginału[cite: 2]
sorted_games = sorted(computer_games)

i = 0
while i < len(sorted_games):
    # Numerujemy pozycje od 1 (i + 1)[cite: 2]
    print(f"{i + 1}. {sorted_games[i]}")
    i += 1
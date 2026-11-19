# Zadanie 2-2
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

# Wypisujemy planszę wiersz po wierszu, oddzielając pola spacją[cite: 8]
for row in tic_tac_toe_board:
    for cell in row:
        print(cell, end=" ")
    print()
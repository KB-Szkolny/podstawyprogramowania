import random  #Importuje moduł random do generowania liczb losowych

dice_roll_1 = random.randint(1, 6)  # Losuje pierwszą liczbę od 1 do 6
dice_roll_2 = random.randint(1, 6)  # ...Drugą liczbę...
dice_roll_3 = random.randint(1, 6)  # ...Trzecią liczbę...

total = dice_roll_1 + dice_roll_2 + dice_roll_3  #Oblicza sumę wyrzuconych oczek

print(f'Three dice rolls: {dice_roll_1}, {dice_roll_2}, {dice_roll_3}')  #Wypisuje wyniki kolejnych rzutów
print(f'Sum of dice rolled: {total}')     #Wypisuje sumę wyrzuconych oczek 
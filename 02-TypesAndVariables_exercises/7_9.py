import random  # Importuje moduł 'random' do generowania liczb losowych

dice_roll = random.randint(1, 6)  # Losuje wynik rzutu kością 
is_special = dice_roll == 1 or dice_roll == 6  # Sprawdza czy wypadła 1 lub 6 

print(f'Dice rolled: {dice_roll}')  # Wypisuje wylosowaną liczbę
print(f'Special number (1 or 6): {is_special}')  # Wypisuje czy liczba jest specjalna 
import random  # Importuje moduł 'random' do generowania liczb losowych

print("Dice rolling simulator")  # Wypisuje nagłówek programu

for i in range(5):                # Pętla wykonuje się 5 razy (dla i od 0 do 4)
    dice_roll = random.randint(1, 6)  # Losuje liczbę od 1 do 6 (rzut kością)
    print(dice_roll, end=" ")    # Wypisuje wylosowaną liczbę, rozdzielając wyniki spacją zamiast nową linią
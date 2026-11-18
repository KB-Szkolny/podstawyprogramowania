# Generates and prints a random number between 1 and 6,
# similar to rolling a dice

import random  # Importuje wbudowany moduł 'random' do generowania liczb pseudolosowych

generate_number = random.randint(1, 6)  # Losuje liczbę całkowitą z przedziału od 1 do 6 włącznie
print("Generated number between 1 - 6 is ", generate_number)  # Wypisuje wylosowaną liczbę w konsoli
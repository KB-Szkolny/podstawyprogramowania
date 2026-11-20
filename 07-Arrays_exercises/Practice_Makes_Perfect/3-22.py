# Zadanie 3-22
import random

def rand_elem(array):
    # Zwracamy losowo wybrany element tablicy
    return random.choice(array)

sample_arr = ["apple", "banana", "cherry", "date", "elderberry"]

for i in range(4):
    print(f"Random pick {i + 1}: {rand_elem(sample_arr)}")
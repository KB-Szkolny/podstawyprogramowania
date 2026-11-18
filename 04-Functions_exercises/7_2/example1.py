# Definicja funkcji dodającej dwie liczby a i b
def add(a, b):
    return a + b

# Definicja funkcji odejmującej liczbę b od liczby a
def subtract(a, b):
    return a - b

# Blok uruchomieniowy – kod poniżej wykona się TYLKO wtedy,
# gdy uruchomisz ten plik bezpośrednio (nie wykona się przy imporcie do innego pliku)
if __name__ == "__main__":
    # Przypisanie wartości testowych do zmiennych
    x = 10
    y = 5
    
    # Wywołanie funkcji i wypisanie wyników w konsoli
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")
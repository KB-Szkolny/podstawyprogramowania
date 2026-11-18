def is_in_range(number, x, y):          # Definicja funkcji sprawdzającej, czy liczba mieści się w przedziale <x, y>
    return x <= number <= y             # Zwraca True, jeśli liczba jest większa lub równa x oraz mniejsza lub równa y

if __name__ == "__main__":              # Kod testowy przy bezpośrednim uruchomieniu pliku
    print(is_in_range(7, 2, 15))        # Wynik testu: True
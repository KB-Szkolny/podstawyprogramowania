def main():
    # Słownik z cennikiem ubrań (klucz: nazwa produktu, wartość: cena przed obniżką)
    price_list = {
        'T-shirt': 19.99,
        'Jeans': 49.99,
        'Jacket': 89.99,
        'Sneakers': 59.99,
        'Hat': 15.99
    }

    # 1. Wyświetlenie cennika przed rabatem
    print("Prices before discount:")
    for item, price in price_list.items():                  # Pobiera parę (nazwa, cena) z każdego elementu
        print(f"{item}: {price:.2f}")                       # :.2f formatuje kwotę do 2 miejsc po przecinku

    # 2. Obliczenie i wyświetlenie łącznej wartości towarów przed obniżką
    total_before = sum(price_list.values())                 # .values() wyciąga same ceny, a sum() je zlicza
    print(f"Total value before discount: {total_before:.2f}\n")

    # 3. Modyfikacja cen bezpośrednio w słowniku (rabat 10%)
    for item in price_list:                                 # Pętla przechodzi po samych kluczach (nazwach ubrań)
        discounted_price = price_list[item] * 0.90          # Obniżka o 10% oznacza 90% ceny wyjściowej
        price_list[item] = round(discounted_price, 2)       # Zaokrągla do 2 miejsc i zapisuje nową cenę w słowniku

    # 4. Wyświetlenie zaktualizowanego cennika po obniżce
    print("Prices after 10% discount:")
    for item, price in price_list.items():
        print(f"{item}: {price:.2f}")

    # 5. Obliczenie i wyświetlenie nowej łącznej wartości po rabacie
    total_after = sum(price_list.values())
    print(f"Total value after discount: {total_after:.2f}")

if __name__ == "__main__":
    main()
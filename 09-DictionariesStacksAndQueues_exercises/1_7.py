def main():
    # Słownik ze stanem magazynowym (produkt -> liczba sztuk)
    products = {
        'Laptop': 15, 'Desktop PC': 10, 'Monitor': 25,
        'Keyboard': 50, 'Mouse': 60, 'External Hard Drive': 30,
        'Printer': 12, 'Router': 20, 'USB Flash Drive': 100,
        'Graphics Card': 8
    }

    total_quantity = 0                      # Licznik łącznej liczby wszystkich produktów

    # Wypisanie każdego produktu i zsumowanie sztuk w magazynie
    for product, quantity in products.items():
        print(f"{product}: {quantity}")
        total_quantity += quantity          # Dodaje ilość bieżącego produktu do sumy

    # Wyświetlenie łącznego stanu magazynowego
    print(f"\nTotal number of products: {total_quantity}")

if __name__ == "__main__":
    main()
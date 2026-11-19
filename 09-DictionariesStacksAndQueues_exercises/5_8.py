# Program oblicza łączną wartość zakupów w koszyku (cart) na podstawie
# cen jednostkowych zapisanych w słowniku prices.

def main():
    # Cennik produktów (produkt -> cena jednostkowa)
    prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

    # Koszyk zakupowy (produkt -> liczba sztuk)
    cart = {'juice': 3, 'bread': 1, 'milk': 2}

    total_cost = 0.0

    # Dla każdego produktu w koszyku mnoży jego ilość przez cenę z cennika
    for item, quantity in cart.items():
        if item in prices:
            total_cost += prices[item] * quantity

    print(f"Total cost of the shopping cart: {total_cost:.2f}")

if __name__ == "__main__":
    main()
# Zadanie 4-10
# Plik clothing.csv zawiera dane o ubraniach.
clothing_file = "clothing.csv"

# Produkty są wczytywane z pliku CSV.
with open(clothing_file, "r", encoding="utf-8", newline="") as file:
    # Każdy produkt zawiera nazwę, cenę i liczbę sztuk w magazynie.
    for product in csv.DictReader(file):
        # Cena i stan magazynowy są zamieniane na liczby przed porównaniem.
        price = float(product["Price"])
        stock = int(product["Stock_Quantity"])
        # Wynik obejmuje produkty tańsze niż 60 i dostępne w liczbie mniejszej niż 40.
        if price < 60 and stock < 40:
            print(
                f'{product["Product_Name"]} '
                f'(price: {price:.2f}, stock: {stock})'
            )

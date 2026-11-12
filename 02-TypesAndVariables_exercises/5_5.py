price = float(input("Enter price: "))           # Pobiera cenę z klawiatury i zmienia na float
discount_percent = float(input("Enter discount %: "))  # Pobiera procent zniżki i zmienia na float

reduction = price * (discount_percent / 100)    # Oblicza kwotę obniżki w zł
price_with_discount = price - reduction         # Oblicza końcową cenę po odjęciu zniżki

print(f"Price with discount: {price_with_discount:.2f}")  # Drukuje nową cenę (2 miejsca po przecinku)
print(f"Reduction: {reduction:.2f}")            # Drukuje wartość obniżki (2 miejsca po przecinku)
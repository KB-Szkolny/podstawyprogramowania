# Zadanie 1-13
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# Mnożymy cenę każdego produktu przez jego liczbę sztuk i sumujemy całość[cite: 6]
total_value = sum(price * qty for price, qty in zip(product_prices, product_quantities))

print(f"Total value of all goods: {total_value:.2f}")
# Zadanie 1-12
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Znajdujemy najwyższy wydatek i odczytujemy jego indeks
max_expense = max(expenses)
max_index = expenses.index(max_expense)

print(f"Most expensive category: {categories[max_index]} ({max_expense})")
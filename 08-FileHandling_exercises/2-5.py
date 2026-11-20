# Zadanie 2-5
# Lista zakupów jest zapisywana w pliku shopping_list.txt w folderze projektu.
shopping_list = "shopping_list.txt"


def add_product(file_name: str, product_name: str) -> None:
    """Dopisz jeden produkt na końcu listy zakupów."""
    # Produkt jest dopisywany do listy, a wcześniejsze wpisy pozostają bez zmian.
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{product_name}\n")


# Program przyjmuje kolejne produkty, aż użytkownik wpisze 0.
while True:
    product = input("Enter product name (0 stops): ")
    if product == "0":
        break
    # Każdy produkt jest zapisywany od razu po wpisaniu.
    add_product(shopping_list, product)

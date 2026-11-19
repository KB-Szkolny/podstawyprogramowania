# Program pobiera z klawiatury nazwę, cenę oraz status zapłaty produktu,
# konwertuje je na odpowiednie typy (str, float, bool) i zapisuje w product.json.

import json

def main():
    product = {}                                # Pusty słownik, do którego trafią dane produktu

    # Odczyt danych od użytkownika i zapisanie ich z odpowiednimi typami danych
    product["name"] = input("Enter product name: ").strip()                 # Nazwa produktu (str)
    product["price"] = round(float(input("Enter product price: ")), 2)      # Cena zaokrąglona do 2 miejsc (float)
    paid_input = input("Is the product paid? (yes/no): ").strip().lower()
    product["paid"] = (paid_input == "yes")                                 # Porównanie zwraca True lub False (bool)

    file_name = "09-DictionariesStacksAndQueues_exercises/product.json"

    # Zapis gotowego słownika produktu do pliku JSON
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(product, file, indent=4, ensure_ascii=False)

    print("Product saved:", product)            # Wyświetla zapisany słownik dla potwierdzenia

if __name__ == "__main__":
    main()
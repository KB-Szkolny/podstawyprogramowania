# Program wyświetla nazwy hoteli oraz oblicza średnią cenę pokoju w Krakowie i Sopocie,
# a następnie wskazuje, w którym z tych miast hotele są tańsze.

def hotel_list(hotels):
    # Tworzy listę samych nazw hoteli i łączy je przecinkami w jeden napis
    names = [hotel["name"] for hotel in hotels]
    return ",".join(names)

def avg_price(hotels):
    # Sumuje ceny wszystkich hoteli z listy i dzieli przez ich liczbę, zaokrąglając do liczby całkowitej
    total = sum(hotel["price"] for hotel in hotels)
    return round(total / len(hotels))

def main():
    hotels_in_Krakow = [
        {"name": "Sky", "price": 320.00},
        {"name": "Metropol", "price": 480.00},
        {"name": "New Port", "price": 420.00},
        {"name": "Aparthotel", "price": 390.00}
    ]

    hotels_in_Sopot = [
        {"name": "Focus", "price": 510.00},
        {"name": "Aqua", "price": 345.00},
        {"name": "La Boutique", "price": 390.00},
        {"name": "Marina", "price": 410.00}
    ]

    # Obliczenie średnich cen dla obu miast
    avg_krakow = avg_price(hotels_in_Krakow)
    avg_sopot = avg_price(hotels_in_Sopot)

    # Wyświetlenie listy hoteli i średnich cen
    print(f"Hotels in Krakow: {hotel_list(hotels_in_Krakow)}")
    print(f"Average hotel price in Krakow: {avg_krakow}")
    print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
    print(f"Average hotel price in Sopot: {avg_sopot}")

    # Wskazanie miasta z niższą średnią ceną
    if avg_krakow < avg_sopot:
        print("Cheaper hotels in: Krakow")
    elif avg_sopot < avg_krakow:
        print("Cheaper hotels in: Sopot")
    else:
        print("Cheaper hotels in: Both cities have the same average price")

if __name__ == "__main__":
    main()
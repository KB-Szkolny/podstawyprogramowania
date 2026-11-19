# Program analizuje listę rezerwacji hotelowych z pliku reservations.json
# i wyświetla liczbę pokoi oraz statystyki opłaconych i nieopłaconych rezerwacji.

import json

def load_reservations(filename):
    # Wczytuje dane z pliku JSON i zwraca listę słowników z rezerwacjami
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Obsługuje strukturę ze słownikiem głównym ('reservations') lub bezpośrednio z listą
    return data["reservations"] if isinstance(data, dict) else data

def count_paid(reservations, paid_status):
    # Zlicza rezerwacje o wskazanym statusie płatności (True = opłacone, False = nieopłacone)
    return sum(1 for r in reservations if r["paid"] == paid_status)

def total_value(reservations, paid_status):
    # Oblicza łączną wartość pobytów (liczba nocy * cena za noc) dla wybranego statusu płatności
    return sum(r["nights"] * r["price_per_night"] for r in reservations if r["paid"] == paid_status)

def main():
    reservations = load_reservations('09-DictionariesStacksAndQueues_exercises/reservations.json')

    # Wyświetlenie pełnego podsumowania wyliczonego przez funkcje pomocnicze
    print(f"Number of rooms: {len(reservations)}")
    print(f"Number of paid reservations: {count_paid(reservations, True)}")
    print(f"Number of unpaid reservations: {count_paid(reservations, False)}")
    print(f"Total value of paid reservations: {total_value(reservations, True):.2f}")
    print(f"Total value of unpaid reservations: {total_value(reservations, False):.2f}")

if __name__ == "__main__":
    main()
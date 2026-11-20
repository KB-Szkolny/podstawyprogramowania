# Zadanie 1-7
# Plik car_park.txt zawiera dzienną liczbę zaparkowanych samochodów.
car_park_file = "car_park.txt"

# Wartości z pliku są zamieniane na liczby i sumowane.
with open(car_park_file, "r", encoding="utf-8") as file:
    daily_counts = [int(line) for line in file]

# Wynik pokazuje łączną liczbę samochodów ze wszystkich dni.
print("Total cars parked:", sum(daily_counts))

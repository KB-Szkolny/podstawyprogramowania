# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.

distance = int(input('Enter distance in km: '))          # Pobiera dystans w km jako liczbę całkowitą (int)
fuel_price = float(input('Enter fuel price per liter: '))      # Pobiera cenę paliwa za litr jako liczbę z przecinkiem (float)
fuel_consumption = float(input('Enter fuel consumption in liters per 100 km: ')) # Pobiera średnie spalanie na 100 km

total_fuel_consumption = (distance * fuel_consumption) / 100    # Oblicza ile litrów paliwa zostanie zużyte na całym dystansie
total_cost = total_fuel_consumption * fuel_price      # Oblicza łączny koszt przejazdu

print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')    # Wypisuje zużycie paliwa zaokrąglone do 2 miejsc po przecinku
print(f'Total transport cost: {total_cost:.2f}')     # Wypisuje całkowity koszt transportu
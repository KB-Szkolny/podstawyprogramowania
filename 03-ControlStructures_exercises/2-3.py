###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode = input('Enter driving mode (A/M/E):')  # Wypisuje komunikat proszący użytkownika o wpisanie trybu jazdy i przypisuje wpisany tekst do zmiennej driving_mode
distance = int(input('Enter distance in km'))  # Wypisuje komunikat proszący użytkownika o wpisanie odległości w km, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej distance

if driving_mode == 'A':  # Sprawdza warunek: czy tryb jazdy (driving_mode) jest równy 'A' (Auto)
    fuel_consumption = 7  # Jeśli warunek jest prawdziwy, przypisuje wartość 7 do zmiennej fuel_consumption (litry na 100 km)
elif driving_mode == 'M':  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy tryb jazdy jest równy 'M' (Manual)
    fuel_consumption = 9  # Jeśli warunek jest prawdziwy, przypisuje wartość 9 do zmiennej fuel_consumption
elif driving_mode == 'E':  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy tryb jazdy jest równy 'E' (Eco)
    fuel_consumption = 6  # Jeśli warunek jest prawdziwy, przypisuje wartość 6 do zmiennej fuel_consumption
else:  # Jeśli żaden z powyższych warunków nie jest prawdziwy, czyli tryb jazdy jest niepoprawny
    print('Incorrect driving mode')  # Wypisuje komunikat o niepoprawnym trybie jazdy

total_consumption = distance/100*fuel_consumption  # Oblicza całkowite zużycie paliwa, dzieląc odległość przez 100 i mnożąc przez zużycie na 100 km
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')  # Wypisuje całkowite zużycie paliwa dla podanej odległości i trybu jazdy

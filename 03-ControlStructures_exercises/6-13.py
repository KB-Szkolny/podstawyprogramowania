car_speed = int(input("Enter car speed (km/h): "))  # Wypisuje komunikat proszący użytkownika o wpisanie prędkości samochodu w km/h, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej car_speed

speed_limit_min = 40  # Przypisuje wartość 40 do zmiennej speed_limit_min, która przechowuje minimalną doпустимą prędkość
speed_limit_max = 140  # Przypisuje wartość 140 do zmiennej speed_limit_max, która przechowuje maksymalną doпустимą prędkość

if car_speed < speed_limit_min or car_speed > speed_limit_max:  # Sprawdza warunek: czy prędkość samochodu (car_speed) jest mniejsza niż minimalna (speed_limit_min) LUB większa niż maksymalna (speed_limit_max)
    print("Warning: Invalid car speed!!")  # Jeśli warunek jest prawdziwy, wypisuje ostrzeżenie o nieprawidłowej prędkości samochodu
elif car_speed >= speed_limit_min and car_speed <= speed_limit_max:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy prędkość jest większa lub równa minimalnej ORAZ mniejsza lub równa maksymalnej
    print("Valid car speed")  # Jeśli warunek jest prawdziwy, wypisuje że prędkość samochodu jest prawidłowa
speed_limit = 140  # Przypisuje wartość 140 do zmiennej speed_limit, która przechowuje dopuszczalny limit prędkości
car_speed = int( input('Enter car speed (km/h): ') )  # Wypisuje komunikat proszący użytkownika o podanie prędkości, pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej car_speed

if car_speed >=140:  # Sprawdza warunek: czy prędkość samochodu (car_speed) jest większa lub równa 140
    print(f'Your speed is {car_speed}km/h')  # Jeśli warunek jest prawdziwy, wypisuje aktualną prędkość samochodu
    print('Warning: speed limit exceeded!!')  # Wypisuje ostrzeżenie o przekroczeniu limitu prędkości
else:  # Jeśli warunek (car_speed >= 140) jest fałszywy, czyli prędkość jest mniejsza niż 140
    print(f'Your speed is {car_speed}km/h')  # Wypisuje aktualną prędkość samochodu
    print('You are driving safely')  # Wypisuje komunikat informujący, że kierowca jedzie bezpiecznie
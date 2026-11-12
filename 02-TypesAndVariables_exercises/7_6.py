vehicle_speed = int(input('Enter vehicle speed in km/h: '))  #Pobiera prędkość i konwertuje tekst na liczbę całkowitą 
is_valid = vehicle_speed >= 40 and vehicle_speed <=140   #Sprawdza czy prędkość mieści się w przedziale 
print(f'Speed is valid: {is_valid}')  #Wypisuje wynik
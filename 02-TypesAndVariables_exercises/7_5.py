car_number = input('Enter car registration number: ')  # Pobiera numer rejestracyjny
is_krakow = car_number[0:2] == "KR" or  car_number[0:2] == "KK"  #Sprawdza czy pierwsze 2 litery [0:2] to "KR" LUB "KK"
print(f'Car is from Krakow: {is_krakow}')  #Wyniik
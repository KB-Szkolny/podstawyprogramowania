
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house

light_switch1 = input('Is the first light switch on? (Y/N): ')  # Wypisuje komunikat pytający czy pierwszy włącznik jest włączony, pobiera odpowiedź użytkownika i przypisuje do zmiennej light_switch1
light_switch2 = input('Is the second light switch on? (Y/N): ')  # Wypisuje komunikat pytający czy drugi włącznik jest włączony, pobiera odpowiedź użytkownika i przypisuje do zmiennej light_switch2

if light_switch1 == 'Y' or light_switch1 == 'y':  # Sprawdza warunek: czy odpowiedź dla pierwszego włącznika jest równa 'Y' LUB 'y'
    light_switch1 = True  # Jeśli warunek jest prawdziwy, przypisuje wartość True do zmiennej light_switch1
else:  # Jeśli warunek jest fałszywy, czyli włącznik nie jest włączony
    light_switch1 = False  # Przypisuje wartość False do zmiennej light_switch1

if light_switch2 == 'Y' or light_switch2 == 'y':  # Sprawdza warunek: czy odpowiedź dla drugiego włącznika jest równa 'Y' LUB 'y'
    light_switch2 = True  # Jeśli warunek jest prawdziwy, przypisuje wartość True do zmiennej light_switch2
else:  # Jeśli warunek jest fałszywy, czyli włącznik nie jest włączony
    light_switch2 = False  # Przypisuje wartość False do zmiennej light_switch2

bulbs_on = 0  # Przypisuje wartość 0 do zmiennej bulbs_on, która liczy aktywne żarówki

if light_switch1:  # Sprawdza warunek: czy pierwszy włącznik jest włączony (True)
    bulbs_on += 1  # Jeśli warunek jest prawdziwy, zwiększa licznik żarówek o 1
if light_switch2:  # Sprawdza warunek: czy drugi włącznik jest włączony (True)
    bulbs_on += 2  # Jeśli warunek jest prawdziwy, zwiększa licznik żarówek o 2
# if light_switch1 and light_switch2:  # Skomentowany kod: sprawdzałoby czy oba włączniki są włączone
#     bulbus_on = 3  # Skomentowany kod: ustawiałoby liczbę żarówek na 3
print(f'Active light bulbs: {bulbs_on}')  # Wypisuje liczbę aktywnych żarówek
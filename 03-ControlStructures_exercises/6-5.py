###
# Program that simulates the operation of an electronic thermometer.
#
temperature = 0  # Przypisuje wartość 0 do zmiennej temperature, która przechowuje temperaturę
if temperature > 35:  # Sprawdza warunek: czy temperatura jest większa niż 35
    print("It is extermely hot")  # Jeśli warunek jest prawdziwy, wypisuje komunikat o ekstremalnym upale
elif temperature > 30:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy temperatura jest większa niż 30
    print("It is hot")  # Jeśli warunek jest prawdziwy, wypisuje komunikat o upale
elif temperature >= 15:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy temperatura jest większa lub równa 15
    print("It is warm ")  # Jeśli warunek jest prawdziwy, wypisuje komunikat o ciepłej pogodzie
elif temperature >= 0:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy temperatura jest większa lub równa 0
    print("It is cold")  # Jeśli warunek jest prawdziwy, wypisuje komunikat o zimnie
elif temperature < 0:  # Jeśli poprzedni warunek jest fałszywy, sprawdza czy temperatura jest mniejsza niż 0
    print("It is really cold")  # Jeśli warunek jest prawdziwy, wypisuje komunikat o bardzo niskiej temperaturze
###
# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):    # Definiuje funkcję przyjmującą numer dnia tygodnia jako parametr
    result = ''         # Tworzy pusty ciąg znaków, do którego trafi nazwa dnia
    if day_number == 1:        # Sprawdza, czy podano 1 (poniedziałek)
        result = 'Monday'
    elif day_number == 2:      # W przeciwnym razie sprawdza, czy podano 2 (wtorek)
        result = 'Tuesday'
    elif day_number == 3:                
        result = 'Wednesday'
    elif day_number == 4:            
        result = 'Thursday'
    elif day_number == 5:                  
        result = 'Friday'
    elif day_number == 6:                
        result = 'Saturday'
    elif day_number == 7:                  
        result = 'Sunday'
    return result          # Zwraca dopasowaną nazwę dnia tygodnia na zewnątrz funkcji

# Function usage
print('The name of day 5 in the week is', day_name(5))  # Wywołuje funkcję dla 5 i wypisuje wynik ('Friday')
print('The name of day 3 in the week is', day_name(3))  # Wywołuje funkcję dla 3 i wypisuje wynik ('Wednesday')
print('The name of day 7 in the week is', day_name(7))  # Wywołuje funkcję dla 7 i wypisuje wynik ('Sunday')
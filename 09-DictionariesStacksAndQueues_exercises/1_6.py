def main():                                             # Główna funkcja programu
    phone_book = {                                      # Słownik: imię (klucz) -> numer telefonu (wartość)
        'John': '555-1234',                             # Wpis w książce telefonicznej
        'David': '555-5678',                            
        'Bob': '555-8765',                              
        'Charlie': '555-4321',                          
        'Diana': '555-9876',                            
        'Eve': '555-6543',                              
        'Frank': '555-3456',                            
        'Grace': '555-7890',                            
        'Hank': '555-1111',                            
        'Ivy': '555-2222',                              
        'Jack': '555-3333',                             
        'Daniel': '555-4444',                           
        'Liam': '555-5555',                             
        'Mia': '555-6666',                              
        'Nina': '555-7777',                             
        'Oscar': '555-8888',                            
        'Paul': '555-9999',                             
        'Dominic': '555-1010',                          
        'Rachel': '555-2020',                           
        'Sam': '555-3030'                               
    }

    for name, number in phone_book.items():             # Iteracja po parach (imię, numer)
        if name.startswith('D'):                        # Sprawdzenie, czy imię zaczyna się od 'D'
            print(f"{name}: {number}")                  # Wypisanie dopasowanego imienia i numeru

if __name__ == "__main__":                              # Punkt startowy programu
    main()                                              # Wywołanie głównej funkcji
def main():                                                         # Główna funkcja programu
    person = {                                                      # Słownik z danymi osoby (str, int, list, bool, dict)
        "name": "Marek",                                            # Imię (str)
        "surname": "Banach",                                        # Nazwisko (str)
        "age": 25,                                                  # Wiek (int)
        "hobby": ["swimming", "excursions"],                        # Lista zainteresowań (list)
        "married": True,                                            # Stan cywilny (bool)
        "phone": {"landline": "123444321", "mobile": "777888999"}   # Zagnieżdżony słownik z telefonami (dict)
    }

    print("Name:", person["name"])                                  # 1. Wyświetlenie imienia
    print("Hobby:", person["hobby"])                                # 2. Wyświetlenie hobby
    print("Initial dictionary:", person)                            # 3. Wyświetlenie całego słownika

    person["surname"] = "Nowak"                                     # 4. Zmiana nazwiska na 'Nowak'
    person["married"] = not person["married"]                       # 5. Zmiana stanu cywilnego na przeciwny
    person["gender"] = "male"                                       # 6. Dodanie nowego klucza 'gender'
    person["hobby"].append("bicycle")                               # 7. Dopisanie 'bicycle' do listy hobby
    person["phone"]["work"] = "313131444"                           # 8. Dodanie telefonu służbowego do słownika 'phone'

    print("\nUpdated dictionary:")                                  # Nagłówek przed wyświetleniem zmian
    for key, value in person.items():                               # 9. Iteracja po wszystkich parach klucz-wartość
        print(f"{key} : {value}")                                   # Wyświetlenie każdej pary w osobnej linii

if __name__ == "__main__":                                          # Punkt startowy programu
    main()                                                          # Wywołanie głównej funkcji
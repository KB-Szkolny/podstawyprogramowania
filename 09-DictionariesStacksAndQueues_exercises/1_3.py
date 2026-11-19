def main():                                     # Główna funkcja programu
    mobile = {                                  # Utworzenie słownika z 6 parami klucz-wartość
        "OS": "Android",                        # System operacyjny
        "Brand": "Samsung",                     # Marka telefonu
        "Model": "Galaxy S24",                  # Model telefonu
        "RAM": "8 GB",                          # Pamięć operacyjna RAM
        "Storage": "256 GB",                    # Pamięć wewnętrzna
        "Color": "Black"                        # Kolor obudowy
    }

    for key, value in mobile.items():           # Pętla po parach (klucz, wartość) ze słownika
        print(f"{key} : {value}")               # Wyświetlenie klucza i wartości w konsoli

if __name__ == "__main__":                      # Punkt startowy programu
    main()                                      # Wywołanie głównej funkcji
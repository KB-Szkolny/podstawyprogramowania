def f(detector):                        # Definicja funkcji sprawdzającej liczbę osób w pokoju
    people_in_room = 0                  # Aktualna liczba osób w pokoju (na start 0)

    for event in detector:              # Przechodzimy przez każde zdarzenie (wejście/wyjście)
        if event == "+":                # Jeśli ktoś wszedł do pokoju (+)
            people_in_room += 1         # Zwiększamy licznik osób o 1
            if people_in_room >= 3:     # Jeśli w pokoju są jednocześnie co najmniej 3 osoby
                return True             # Od razu zwracamy True
        elif event == "-":              # Jeśli ktoś wyszedł z pokoju (-)
            people_in_room -= 1         # Zmniejszamy licznik osób o 1

    return False                        # Jeśli nigdy nie było min. 3 osób naraz, zwracamy False

def main():                             # Główna funkcja testująca
    print(f("+-+++-+---"))              # Osiąga 3 osoby -> True
    print(f("+-+-+-+-"))                # Maksymalnie 1 osoba -> False
    print(f("+-++-+--"))                # Maksymalnie 2 osoby -> False
    print(f("+-++-++-+---"))            # Osiąga 3 osoby -> True

if __name__ == "__main__":              # Uruchomienie main() przy bezpośrednim starcie pliku
    main()
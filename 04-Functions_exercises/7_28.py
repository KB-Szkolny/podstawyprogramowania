def f(dice):                    # Definicja funkcji sprawdzającej najdłuższą serię rzutów
    max_streak = 1         # Rekordowa długość serii (na start 1)
    current_streak = 1           # Licznik aktualnej serii takich samych oczek
    best_digit = int(dice[0])       # Zwycięska cyfra (na start pierwsza z ciągu)

    for i in range(1, len(dice)):       # Pętla po wszystkich znakach od drugiego do końca
        if dice[i] == dice[i - 1]:      # Sprawdzenie, czy obecny rzut jest taki sam jak poprzedni
            current_streak += 1         # Wydłużenie aktualnej serii o 1
            if current_streak > max_streak:     # Sprawdzenie, czy pobiliśmy dotychczasowy rekord
                max_streak = current_streak     # Zapisanie nowej rekordowej długości
                best_digit = int(dice[i])       # Zapisanie cyfry, która ustanowiła rekord
        else:                           # Jeśli wypadła inna liczba niż poprzednio
            current_streak = 1          # Reset licznika aktualnej serii do 1

    return best_digit           # Zwrócenie cyfry wyrzuconej najwięcej razy z rzędu

def main():                      # Główna funkcja testująca działanie programu
    print(f("5233165554211"))        # Wyświetlenie wyniku dla pierwszego ciągu (wynik: 5)
    print(f("2133"))               # Wyświetlenie wyniku dla drugiego ciągu (wynik: 3)

if __name__ == "__main__":      # Uruchomienie main() tylko przy bezpośrednim odpaleniu pliku
    main()
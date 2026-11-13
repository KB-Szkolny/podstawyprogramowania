###
# Sums numbers entered by user
#
total_sum = 0  # Przypisuje wartość 0 do zmiennej total_sum, która będzie przechowywać sumę wszystkich liczb
counter = 0  # Przypisuje wartość 0 do zmiennej counter, która będzie liczyć liczbę wpisanych liczb
while True:  # Rozpoczyna nieskończoną pętlę, która wykonuje się w kółko, dopóki nie zostanie przerwana
    number = int(input("Enter a number (0 to stop): "))  # Wypisuje komunikat proszący użytkownika o wpisanie liczby (0 do zatrzymania), pobiera wpisany tekst, konwertuje go na liczbę całkowitą i przypisuje do zmiennej number
    
    if number == 0:  # Sprawdza warunek: czy wpisana liczba (number) jest równa 0
        break  # Jeśli warunek jest prawdziwy, przerywa pętlę (zatrzymuje program)

    counter += 1  # Zwiększa licznik (counter) o 1, co oznacza że użytkownik wpisał kolejną liczbę
    total_sum += number  # Dodaje wpisana liczbę (number) do sumy (total_sum)

average = total_sum/counter  # Oblicza średnią arytmetyczną, dzieląc sumę wszystkich liczb (total_sum) przez ich liczbę (counter)
print(f"The total sum of the numbers is: {total_sum}")  # Wypisuje całkowitą sumę wpisanych liczb
print(f"The average is: {average}")  # Wypisuje średnią arytmetyczną wpisanych liczb
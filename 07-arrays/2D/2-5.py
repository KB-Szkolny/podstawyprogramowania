# Zadanie 2-5
# 5x5 cinema seating: 'A' = Available, 'B' = Booked[cite: 11]
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    # Łączna liczba miejsc na sali[cite: 11]
    return sum(len(row) for row in seats)

def seats_available(seats):
    # Liczba wolnych miejsc ('A')[cite: 11]
    return sum(row.count('A') for row in seats)

def seats_booked(seats):
    # Liczba zajętych miejsc ('B')[cite: 11]
    return sum(row.count('B') for row in seats)

def seat_status(seats, row, place):
    # Numeracja w poleceniu zaczyna się od 1, więc odejmujemy 1 przy indeksowaniu[cite: 11]
    status = seats[row - 1][place - 1]
    return "Available" if status == 'A' else "Booked"

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
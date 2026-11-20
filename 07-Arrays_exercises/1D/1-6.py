# Zadanie 1-6
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    # Indeksy listy zaczynają się od 0, więc dla n=1 zwracamy element o indeksie 0
    return weekdays[n - 1]

# Wypisujemy nazwy dni dla numerów 1, 4 oraz 7
for day_num in [1, 4, 7]:
    print(f"Day {day_num}: {weekday(day_num)}")
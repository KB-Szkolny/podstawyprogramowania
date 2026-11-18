import months                           # Import własnego modułu months.py

def main():                             # Główna funkcja programu
    n = int(input("Enter month number: "))  # Pobranie numeru miesiąca od użytkownika i zamiana na int
    month_name = months.month(n)        # Wywołanie funkcji month() z modułu months
    print(f"The name of month {n} is {month_name}") # Wyświetlenie nazwy miesiąca

if __name__ == "__main__":              # Punkt startowy programu
    main()
import queue  # Moduł udostępniający gotowe struktury kolejek i stosów

def main():
    # Tworzy pusty stos typu LIFO (Last In, First Out – ostatni element wchodzi, pierwszy wychodzi)
    stack = queue.LifoQueue()

    # 1–7. Dodanie kolejnych liczb na wierzch stosu (na samym szczycie znajdzie się ostatnia liczba, czyli 8)
    for number in [2, 3, 7, 4, 1, 9, 8]:
        stack.put(number)               # Metoda .put() kładzie element na szczycie stosu

    # 8. Pobranie dwóch ostatnich liczb ze szczytu stosu i wyświetlenie ich sumy
    last_one = stack.get()              # Metoda .get() zdejmuje i zwraca element ze szczytu (8)
    last_two = stack.get()              # Zdejmuje kolejny element spod spodu (9)
    print(f"Sum of the last two numbers: {last_one + last_two}")

    # 9. Obliczenie sumy pozostałych elementów leżących jeszcze na stosie (2, 3, 7, 4, 1)
    remaining_sum = 0
    while not stack.empty():            # Pętla działa, dopóki metoda .empty() nie zwróci True (stos pusty)
        remaining_sum += stack.get()    # Zdejmuje kolejny element ze stosu i dolicza go do sumy

    print(f"Sum of the remaining elements: {remaining_sum}")

if __name__ == "__main__":
    main()
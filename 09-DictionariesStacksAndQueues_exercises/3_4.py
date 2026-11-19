import queue

def main():
    stack = queue.LifoQueue()

    # Pobranie liczby dziesiętnej od użytkownika i zapisanie jej w zmiennej roboczej temp
    number = int(input("Natural number: "))
    temp = number

    # Przypadek szczególny: dla zera reszta wynosi 0
    if temp == 0:
        stack.put(0)

    # Algorytm zamiany na system dwójkowy: dzielimy przez 2 i zapisujemy reszty na stosie
    # Ponieważ kolejne reszty odczytujemy od końca, stos LIFO idealnie odwróci ich kolejność
    while temp > 0:
        remainder = temp % 2            # Reszta z dzielenia przez 2 daje kolejną cyfrę binarną (0 lub 1)
        stack.put(remainder)            # Odkładamy cyfrę na szczyt stosu
        temp = temp // 2                # Dzielenie całkowite (odrzuca resztę) przygotowuje liczbę do kolejnego kroku

    # Zdejmujemy cyfry ze stosu od góry do dołu i sklejamy w gotowy napis binarny
    binary_number = ""
    while not stack.empty():
        binary_number += str(stack.get())

    print(f"Binary number: {binary_number}")

if __name__ == "__main__":
    main()
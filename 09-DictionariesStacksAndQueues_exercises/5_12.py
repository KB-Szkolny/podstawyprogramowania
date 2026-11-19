# Program definiuje funkcję odwracającą dowolny napis przy użyciu stosu (LIFO)
# i wyświetla odwrócony tekst wpisany przez użytkownika z klawiatury.

import queue

def reverse_string(text):
    stack = queue.LifoQueue()                   # Tworzy pusty stos typu LIFO (ostatni wchodzi, pierwszy wychodzi)

    # Wrzucamy na stos po kolei każdą literę z podanego napisu
    for char in text:
        stack.put(char)

    # Zdejmujemy litery ze szczytu stosu aż do jego opróżnienia – wychodzą w odwrotnej kolejności
    reversed_text = ""
    while not stack.empty():
        reversed_text += stack.get()

    return reversed_text

def main():
    text = input("Enter text to reverse: ")
    print("Reversed text:", reverse_string(text))

if __name__ == "__main__":
    main()
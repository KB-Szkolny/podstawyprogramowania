# Program oblicza wartość wyrażeń zapisanych w odwrotnej notacji polskiej (RPN) za pomocą stosu.
# Użytkownik wpisuje kolejno liczby, operatory (+, -, *, /) oraz znak '=' kończący obliczenia.

import queue

def main():
    stack = queue.LifoQueue()
    print("Enter RPN tokens one by one (numbers, +, -, *, /, or = to finish):")

    while True:
        token = input("> ").strip()

        if token == "=":
            # Znak '=' kończy działanie i zdejmuje ze stosu ostateczny wynik obliczeń
            if not stack.empty():
                print("Result:", stack.get())
            break
        elif token in "+-*/":
            # Zdejmujemy dwie ostatnie liczby ze stosu (pierwsza zdjęta 'b' to prawy argument działania)
            b = stack.get()
            a = stack.get()
            if token == "+":
                stack.put(a + b)                # Wynik działania wraca na wierzch stosu
            elif token == "-":
                stack.put(a - b)
            elif token == "*":
                stack.put(a * b)
            elif token == "/":
                stack.put(a / b)
        else:
            # Każdą wpisaną liczbę zamieniamy na float i odkładamy na stos
            stack.put(float(token))

if __name__ == "__main__":
    main()
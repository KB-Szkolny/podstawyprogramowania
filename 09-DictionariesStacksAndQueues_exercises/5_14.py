# Program symuluje system kolejkowy w urzędzie (FIFO).
# Nadaje kolejnym klientom numery biletów i obsługuje ich w kolejności przyjścia.

import queue

def main():
    customer_queue = queue.Queue()              # Kolejka FIFO (pierwszy klient w kolejce jest obsługiwany pierwszy)
    ticket_number = 1                           # Licznik nadający kolejnym klientom unikalne numery biletów

    while True:
        # Wyświetlenie menu wyboru akcji w systemie kolejkowym
        print("\n1. New customer (take a ticket)")
        print("2. Serve next customer")
        print("0. Quit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            # Dodaje numer nowego klienta na sam koniec kolejki
            customer_queue.put(ticket_number)
            print(f"Customer #{ticket_number} added to the queue.")
            ticket_number += 1                  # Zwiększa numer biletu dla następnego klienta
        elif choice == "2":
            # Sprawdza, czy w kolejce czekają klienci, i wywołuje osobę z samego początku
            if not customer_queue.empty():
                served = customer_queue.get()   # Pobiera i usuwa pierwszy numer z początku kolejki
                print(f"Now serving customer #{served}.")
            else:
                print("The queue is empty. No customers waiting.")
        elif choice == "0":
            break                               # Kończy działanie programu
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
import queue

def main():
    # Stos przechowuje historię odwiedzanych stron w kolejności od najstarszej na dole do najnowszej na górze
    visited_websites = queue.LifoQueue()

    # Dodanie kilku przykładowych stron na start (ostatnia dodana jest na szczycie stosu)
    visited_websites.put('instagram.com')
    visited_websites.put('uek.krakow.pl')
    visited_websites.put('microsoft.com')

    # Nieskończona pętla symulująca ciągłą pracę przeglądarki
    while True:
        website = input('Enter website name (0 for back): ')

        if website == '0':
            # Użytkownik kliknął "Wstecz" (wpisał 0)
            if visited_websites.empty():
                # Jeśli stos jest pusty, nie ma już dokąd wracać – kończymy program
                print("No more websites in history.")
                break
            else:
                # Pobieramy ostatnio zapisaną stronę ze szczytu stosu i usuwamy ją z historii
                print('<-- Going back to a previously visited website')
                website = visited_websites.get()
        elif website != "":
            # Użytkownik wpisał nowy adres – zapisujemy go na wierzchu stosu
            visited_websites.put(website)

        # Wyświetlamy stronę, na której aktualnie znajduje się użytkownik
        print('You are currently viewing:', website)
        print()

if __name__ == "__main__":
    main()
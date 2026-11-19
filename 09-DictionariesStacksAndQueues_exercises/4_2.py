import queue  # Moduł udostępniający gotową strukturę kolejki FIFO

def main():
    # Tworzy pustą kolejkę typu FIFO (First In, First Out – pierwszy wchodzi, pierwszy wychodzi)
    files_to_print = queue.Queue()

    # Nieskończona pętla wyświetlająca menu użytkownika aż do wybrania opcji '0'
    while True:
        print('1. Add file to print')
        print('2. Print file')
        print('0. Quit')
        menu = input('Select an option: ')
        print()

        if menu == '1':
            # Pobiera nazwę pliku od użytkownika i dodaje go na sam koniec kolejki
            file_name = input('Enter file name to print: ')
            files_to_print.put(file_name)       # Metoda .put() wstawia element na koniec kolejki
            print(f'File {file_name} added to the print queue.\n')

        elif menu == '2':
            # Sprawdza, czy w kolejce znajdują się jakiekolwiek pliki oczekujące na wydruk
            if not files_to_print.empty():      # .empty() zwraca True, gdy kolejka jest pusta
                # Pobiera i usuwa pierwszy plik z początku kolejki (ten, który czeka najdłużej)
                file_to_print = files_to_print.get()
                print(f'File {file_to_print} is currently being printed. Please wait!\n')
            else:
                # Komunikat wyświetlany, gdy kolejka drukowania jest pusta
                print('The print queue is empty. No files to print.\n')

        elif menu == '0':
            # Przerywa pętlę while i kończy działanie programu
            break

        else:
            # Obsługa błędnego wyboru w menu
            print('Invalid option. Please select 1, 2, or 0.\n')

if __name__ == "__main__":
    main()
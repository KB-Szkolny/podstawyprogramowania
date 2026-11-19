def main():
    # Lista adresów e-mail zawierająca powtórzenia
    emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]

    # Konwersja listy na zbiór (set) automatycznie usuwa wszystkie duplikaty
    unique_emails = set(emails)

    # Wyświetlenie zbioru unikalnych adresów
    print(unique_emails)

if __name__ == "__main__":
    main()
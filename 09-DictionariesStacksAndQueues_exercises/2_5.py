def main():
    # Dwa zbiory kontaktów pobrane z różnych źródeł
    contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
    contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

    # Suma zbiorów (|) łączy wszystkie elementy z obu zbiorów, zachowując tylko unikalne wpisy
    merged_contacts = contacts_A | contacts_B

    # Wyświetlenie połączonej listy kontaktów
    print("Merged contacts:", merged_contacts)

if __name__ == "__main__":
    main()
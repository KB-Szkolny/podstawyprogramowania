def main():
    # Zbiór odebranych wiadomości oraz zbiór znanych adresów spamowych
    emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
    spam_list = {"spam1@example.com", "spam2@example.com"}

    # Część wspólna (&) wyznacza adresy występujące jednocześnie w obu zbiorach
    spam_emails = emails_received & spam_list

    # Wyświetlenie wykrytych wiadomości spamowych
    print("Spam emails:", spam_emails)

if __name__ == "__main__":
    main()
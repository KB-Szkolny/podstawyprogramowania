def main():
    # Zbiór wymaganych uprawnień oraz zbiór uprawnień posiadanych przez użytkownika
    required_permissions = {"read", "write", "execute"}
    user_permissions = {"read", "write"}

    # Metoda .issubset() sprawdza, czy wszystkie wymagane uprawnienia zawierają się w uprawnieniach użytkownika
    has_permissions = required_permissions.issubset(user_permissions)

    # Zwróci False, ponieważ użytkownikowi brakuje uprawnienia "execute"
    print(has_permissions)

if __name__ == "__main__":
    main()
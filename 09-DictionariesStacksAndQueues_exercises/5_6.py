# Program łączy dane osobowe z dwóch osobnych słowników (basic_data oraz advanced_data)
# w jeden wspólny słownik person i wyświetla jego zawartość.

def main():
    basic_data = {
        "name": "Barbara",
        "age": 21
    }

    advanced_data = {
        "status": "student",
        "married": False,
        "interest": ["reading", "swimming"]
    }

    # Rozpakowanie (**) obu słowników łączy ich wszystkie pary klucz-wartość w jeden słownik
    person = {**basic_data, **advanced_data}

    # Wyświetlenie zawartości połączonego słownika
    print(person)

if __name__ == "__main__":
    main()
# Moduł pomocniczy do zadania 4-5.
"""Funkcje odczytujące elementy wiadomości z pliku email.txt."""
# Wszystkie funkcje pobierają dane z pliku email.txt.
EMAIL_FILE = "email.txt"


def _read_email() -> str:
    """Zwraca całą wiadomość jako tekst UTF-8."""
    # Wiadomość jest odczytywana jako tekst UTF-8.
    with open(EMAIL_FILE, "r", encoding="utf-8") as file:
        return file.read()


def _header_value(header_name: str) -> str:
    """Zwraca wartość wskazanego nagłówka wiadomości."""
    # Wyszukiwanie obejmuje wiersz zaczynający się od nazwy nagłówka.
    pattern = rf"^{re.escape(header_name)}:\s*(.*?)\s*$"
    match = re.search(pattern, _read_email(), flags=re.IGNORECASE | re.MULTILINE)
    # Zwracana jest wartość po dwukropku lub pusty tekst, jeśli nagłówka nie ma.
    return match.group(1) if match else ""


def email_sender() -> str:
    """Zwraca adres nadawcy."""
    # Adres jest pobierany z zapisu „Imię Nazwisko <adres>”.
    address = re.search(r"<([^<>]+)>", _header_value("From"))
    # Jeśli nawiasów nie ma, zwracana jest cała zawartość nagłówka.
    return address.group(1) if address else _header_value("From")


def email_recipient() -> str:
    """Zwraca adres odbiorcy."""
    # Adres odbiorcy pochodzi z nagłówka To.
    address = re.search(r"<([^<>]+)>", _header_value("To"))
    return address.group(1) if address else _header_value("To")


def email_subject() -> str:
    """Zwraca temat wiadomości."""
    # Temat pochodzi z nagłówka Subject.
    return _header_value("Subject")


def email_body() -> str:
    """Zwraca treść wiadomości znajdującą się za nagłówkami."""
    # Pierwsza pusta linia oddziela treść od nagłówków.
    parts = re.split(r"\r?\n\r?\n", _read_email(), maxsplit=1)
    # Zwracana treść nie zawiera pustych znaków na początku ani na końcu.
    return parts[1].strip() if len(parts) == 2 else ""

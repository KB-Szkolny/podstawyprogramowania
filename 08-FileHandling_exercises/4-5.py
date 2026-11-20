# Zadanie 4-5
# Program wyświetla nadawcę, odbiorcę, temat i treść odczytane przez moduł emails.
from emails import email_sender, email_recipient, email_subject, email_body  # import funkcji z modułu emails do odczytu poszczególnych części wiadomości
print("Sender:", email_sender())
print("Recipient:", email_recipient())
print("Subject:", email_subject())
print("Body:")
# Treść może składać się z kilku wierszy.
print(email_body())

# Definiuje tekst, w którym będą zliczane samogłoski
text = "This is a sample text."

# Definiuje ciąg zawierający wszystkie poszukiwane samogłoski (małe i wielkie litery)
vowels = "aeiouAEIOU"

# Inicjalizuje licznik samogłosek, ustawiając go na początkową wartość 0
vowel_count = 0

# Inicjalizuje zmienną indeksową 'i' wartością 0 (będzie służyć do przechodzenia przez kolejne znaki tekstu)
i = 0

# Pętla 'while' wykonuje się tak długo, dopóki indeks 'i' jest mniejszy niż długość całego tekstu
while i < len(text):
  # Sprawdza, czy znak w tekście pod aktualnym indeksem 'i' znajduje się w zbiorze samogłosek
  if text[i] in vowels:
    # Jeśli tak, zwiększa licznik samogłosek o 1
    vowel_count += 1
  # Zwiększa indeks o 1, aby w kolejnym obiegu pętli sprawdzić następny znak tekstu
  i += 1

# Wyświetla ostateczny komunikat z podsumowaniem liczby samogłosek w tekście
print(f"The number of vowels in the text is: {vowel_count}")

# --- Oryginalna wersja z pętlą 'for' (pozostawiona w komentarzu jako odniesienie): ---
# Count vowels in the text
# for char in text:
#     if char in vowels:
#         vowel_count += 1
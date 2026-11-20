# Zadanie 4-7
# Tekst pochodzi od użytkownika i jest sprawdzany pod kątem samogłosek.
text = input("Enter text: ")
# Wyrażenie regularne znajduje samogłoski niezależnie od wielkości liter.
vowels = re.findall(r"[aeiou]", text, flags=re.IGNORECASE)
# Wynik przedstawia liczbę znalezionych samogłosek.
print("Number of vowels:", len(vowels))

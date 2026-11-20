# Zadanie 1-8
# Plik pets.txt zawiera tekst o zwierzętach.
pets_file = "pets.txt"

# Program wczytuje tekst, aby go wyświetlić i policzyć słowa.
with open(pets_file, "r", encoding="utf-8") as file:
    content = file.read()

# Tekst jest wyświetlany bez zbędnej pustej linii na końcu.
print(content, end="" if content.endswith("\n") else "\n")
# Liczba słów obejmuje wyrazy rozdzielone spacjami lub znakami nowej linii.
print("Number of words:", len(content.split()))

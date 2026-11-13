# Pobiera od użytkownika liczbę i konwertuje ją z tekstu na liczbę całkowitą (integer)
x = int(input("Enter your number: "))

# Pętla iteruje przez zmienną 'i' od 1 do 10 włącznie (funkcja range kończy się przed 11)
for i in range(1, 11):
  # Wyświetla sformatowane działanie mnożenia: wprowadzona liczba (x)
  # pomnożona przez aktualną wartość licznika pętli (i) oraz wynik tego mnożenia
  print(f"{x} x {i} = {x * i}")
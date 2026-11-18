# Komentarz zawiera oryginalną wersję kodu z użyciem pętli 'for' (pętla w pętli)
# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f'{i+j}',end=' ')
#     print()

# Inicjalizacja zmiennej zewnętrznej 'i' wartością początkową 6
i = 6

# Zewnętrzna pętla 'while' wykonuje się, dopóki 'i' jest większe od -1 (dla i = 6, 3, 0)
while i > -1:
  # Inicjalizacja zmiennej wewnętrznej 'j' wartością 1 dla każdego nowego obiegu pętli zewnętrznej
  j = 1

  # Wewnętrzna pętla 'while' wykonuje się dla 'j' równego 1, 2 oraz 3 (dopóki j < 4)
  while j < 4:
    # Wyświetla sumę aktualnej wartości 'i' oraz 'j', używając spacji jako separatora (zamiast przejścia do nowej linii)
    print(f"{i+(j)}", end=" ")

    # Zwiększa licznik wewnętrzny 'j' o 1 w każdym kroku pętli
    j += 1

  # Po zakończeniu wewnętrznej pętli wypisuje pusty znak nowej linii, aby przejść do kolejnego wiersza
  print()

  # Zmniejsza wartość zmiennej 'i' o 3 (krok wstecz w pętli zewnętrznej)
  i -= 3
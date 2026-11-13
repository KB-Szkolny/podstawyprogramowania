# Inicjalizuje pierwszą zmienną 'a' wartością 0 (pierwszy wyraz ciągu Fibonacciego)
a = 0

# Inicjalizuje drugą zmienną 'b' wartością 1 (drugi wyraz ciągu Fibonacciego)
b = 1

# Pętla wykonuje się 20 razy (dla i od 0 do 19), generując kolejne wyrazy ciągu
for i in range(20):
  # Wyświetla aktualną wartość zmiennej 'a' i kończy wypisanie spacją (zamiast nowej linii)
  print(a, end=" ")

  # Zakomentowana linia pomocnicza (przydatna podczas testów do podglądu wartości w pętli)
  # print(f'{i}, {a}, {b}')

  # Zapamiętuje obecną wartość 'b' w zmiennej pomocniczej, zanim zmienimy 'b'
  old_b = b

  # Oblicza nową wartość 'b' jako sumę poprzedniej wartości 'b' oraz 'a'
  b = old_b + a

  # Przypisuje starą wartość 'b' do zmiennej 'a' (przesuwa wartości w prawo w kolejnym kroku)
  a = old_b
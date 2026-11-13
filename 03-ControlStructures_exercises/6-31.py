# Importuje wbudowany moduł 'random', który umożliwia generowanie liczb losowych
import random

# Pętla wykonuje się 20 razy (zmienna 'i' przyjmuje wartości od 0 do 19)
for i in range(20):
  # random.randint(5, 10) losuje i zwraca losową liczbę całkowitą
  # z podanego przedziału domkniętego (od 5 do 10 włącznie), a następnie ją wypisuje
  print(random.randint(5, 10))
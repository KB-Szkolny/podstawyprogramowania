# Zadanie 3-7
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = names[0]

# Porównujemy długość imion[cite: 13]
for name in names[1:]:
    if len(name) > len(longest_name):
        longest_name = name

print("Names:", *names)
print("Longest name:", longest_name)
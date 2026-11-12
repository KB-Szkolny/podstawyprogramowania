employee = "Mr. John May, born on 1998-02-16"  # Tworzy zmienną tekstową z danymi pracownika

print(f'Name: {employee[4:8]}')             # Wyciąga imię 'John' (od indeksu 4 do 7)
print(f'Surname: {employee[9:12]}')         # Wyciąga nazwisko 'May' (od indeksu 9 do 11)
print(f'Born: {employee[22:32]}')           # Wyciąga datę '1998-02-16' (od indeksu 22 do 31)
print(f'Initials: {employee[4]}{employee[9]}')  # Łączy pierwsze litery imienia i nazwiska ('JM')
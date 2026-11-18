facebook = True  # Przypisuje wartość True do zmiennej facebook, która oznacza że użytkownik ma konto na Facebooku
twitter = False  # Przypisuje wartość False do zmiennej twitter, która oznacza że użytkownik nie ma konta na Twitterze
instagram = True  # Przypisuje wartość True do zmiennej instagram, która oznacza że użytkownik ma konto na Instagramie

account_amount = 0  # Przypisuje wartość 0 do zmiennej account_amount, która będzie liczyć liczbę kont w mediach społecznościowych

if facebook:  # Sprawdza warunek: czy zmienna facebook ma wartość True
    account_amount += 1  # Jeśli warunek jest prawdziwy, zwiększa licznik kont (account_amount) o 1
if twitter:  # Sprawdza warunek: czy zmienna twitter ma wartość True
    account_amount += 1  # Jeśli warunek jest prawdziwy, zwiększa licznik kont (account_amount) o 1
if instagram:  # Sprawdza warunek: czy zmienna instagram ma wartość True
    account_amount += 1  # Jeśli warunek jest prawdziwy, zwiększa licznik kont (account_amount) o 1
if account_amount >= 2:  # Sprawdza warunek: czy liczba kont (account_amount) jest większa lub równa 2
    print("You are a good influencer!")  # Jeśli warunek jest prawdziwy, wypisuje że użytkownik jest dobrym influencerem
else:  # Jeśli warunek jest fałszywy, czyli liczba kont jest mniejsza niż 2
    print("You are not a good influencer!")  # Wypisuje że użytkownik nie jest dobrym influencerem
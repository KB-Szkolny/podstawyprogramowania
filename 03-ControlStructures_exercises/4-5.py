###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'  # Przypisuje wartość 'The early bird catches the worm' do zmiennej plain_text, która przechowuje tekst jawny
encrypted_text = ''  # Przypisuje pustą wartość do zmiennej encrypted_text, która będzie przechowywać zaszyfrowany tekst

for char in plain_text:  # Rozpoczyna pętlę, która iteruje przez każdy znak (char) w ciągu plain_text
    char_code = ord(char)  # Pobiera kod ASCII aktualnego znaku (char) i przypisuje do zmiennej char_code
    char_code += 1  # Zwiększa kod ASCII o 1, co odpowiada przesunięciu znaku o jedną pozycję w alfabecie
    new_char = chr(char_code)  # Konwertuje nowy kod ASCII z powrotem na znak i przypisuje do zmiennej new_char
    encrypted_text += new_char  # Dodaje nowy znak do zmiennej encrypted_text

print(f'Plain text: {plain_text}')  # Wypisuje tekst jawny
print(f'Encrypted text: {encrypted_text}')  # Wypisuje zaszyfrowany tekst
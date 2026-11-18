###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)     # 2. Zamienia liczbę na wartość bezwzględną (ignoruje znak minus)
    number_str = str(number)    # 3. Konwertuje liczbę na napis (ciąg znaków), aby móc po niej iterować
    total = 0               # Zmienna przechowująca sumę cyfr

    for digit in number_str:    # 4. Pętla przechodząca po każdym znaku (cyfrze) w napisie
        total += int(digit)      # 5. Zamienia znak z powrotem na int i dodaje do bieżącej sumy

    return total        # 6. Zwraca obliczoną sumę cyfr

# 1. Pobranie liczby całkowitej od użytkownika
any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)

print(f'The sum of the digits in the number {any_number} is {result}')
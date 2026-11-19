# Zadanie 1-10
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

question_number = len(test_results)  # łączna liczba pytań[cite: 4]
correct_answers = sum(test_results)  # True działa jak 1, a False jak 0[cite: 4]
incorrect_answers = question_number - correct_answers  # liczba błędnych odpowiedzi[cite: 4]
percentage = (correct_answers / question_number) * 100  # odsetek poprawnych odpowiedzi[cite: 4]

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f'Percentage of correct answers: {percentage:.2f}%')
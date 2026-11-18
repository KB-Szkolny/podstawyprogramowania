###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:   # Sprawdza, czy wynik wynosi co najmniej 18 punktów
        grade = 'Excellent'
    elif points >= 14:     # W przeciwnym razie sprawdza, czy wynik wynosi co najmniej 14 punktów
        grade = 'Good'
    elif points >= 10:    # W przeciwnym razie sprawdza, czy wynik wynosi co najmniej 10 punktów
        grade = 'Satisfactory'
    else:            # Dla wszystkich wyników poniżej 10 punktów
        grade = 'Fail'
    return grade       # Zwraca ustaloną ocenę końcową

test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')
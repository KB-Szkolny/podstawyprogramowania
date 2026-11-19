# Zadanie 3-9
def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for a, b in zip(array1, array2):
        if a != b:
            return False
    return True

test_pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

for arr1, arr2 in test_pairs:
    result_text = "arrays are the same" if compare(arr1, arr2) else "arrays are different"
    print("Array1:", *arr1)
    print("Array2:", *arr2)
    print("Comparison:", result_text)
    print("-" * 30)
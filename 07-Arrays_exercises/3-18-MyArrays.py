# Moduł MyArrays dla zadania 3-18
def _sort_asc(arr):
    copy = arr[:]
    n = len(copy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if copy[j] > copy[j + 1]:
                copy[j], copy[j + 1] = copy[j + 1], copy[j]
    return copy

def second_largest(arr):
    sorted_vals = _sort_asc(arr)
    unique_sorted = []
    for x in sorted_vals:
        if x not in unique_sorted:
            unique_sorted.append(x)
    return unique_sorted[-2] if len(unique_sorted) >= 2 else unique_sorted[-1]

def diff_min_max(arr):
    sorted_vals = _sort_asc(arr)
    return sorted_vals[-1] - sorted_vals[0]

def median(arr):
    sorted_vals = _sort_asc(arr)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 1:
        return sorted_vals[mid]
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2

def min_max_array(arr):
    sorted_vals = _sort_asc(arr)
    return [sorted_vals[0], sorted_vals[-1]]

def join_with_minus(arr):
    return "-".join(str(x) for x in arr)
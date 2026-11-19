# Zadanie 3-18
import MyArrays

numbers = [7, 3, 8, 5, 2]
smallest, largest = MyArrays.min_max_array(numbers)

print("Numbers:", ",".join(map(str, numbers)))
print("Second largest number:", MyArrays.second_largest(numbers))
print("Difference (max - min):", MyArrays.diff_min_max(numbers))
print("Median:", MyArrays.median(numbers))
print(f"Smallest and largest number: {smallest},{largest}")
print("Numbers as a string:", MyArrays.join_with_minus(numbers))
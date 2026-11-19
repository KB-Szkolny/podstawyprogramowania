# Zadanie 3-13
def occurs(number, array):
    return number in array

arr = [15, 38, 7, 23, 14]
num = int(input("Enter a number: "))

print("Number:", num)
print("Array:", *arr)
if occurs(num, arr):
    print(f"Result: number {num} appears in the array")
else:
    print(f"Result: number {num} does not appear in the array")
# Zadanie 3-19
real_numbers = [1.5, 4.2, -3.0, 8.7, 2.3, 10.0, 5.5]
threshold = float(input("Enter a threshold value: "))

# Liczymy elementy większe od wartości podanej z klawiatury[cite: 15]
greater_count = sum(1 for num in real_numbers if num > threshold)

print("Number of elements greater than given value:", greater_count)
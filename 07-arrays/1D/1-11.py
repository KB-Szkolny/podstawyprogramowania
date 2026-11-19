# Zadanie 1-11
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

measurements = len(temperatures)  # liczba pomiarów[cite: 5]
avg_temp = sum(temperatures) / measurements  # średnia temperatura w miesiącu[cite: 5]
min_temp = min(temperatures)  # minimalna temperatura[cite: 5]
max_temp = max(temperatures)  # maksymalna temperatura[cite: 5]

# Liczymy dni z temperaturą ujemną za pomocą pętli while[cite: 5]
negative_temp = 0
i = 0
while i < measurements:
    if temperatures[i] < 0:
        negative_temp += 1
    i += 1

print("TEMPERATURE REPORT")
print("Month: March")
print("Number of measurements:", measurements)
print(f"Average temperature in the month: {avg_temp:.2f}")
print("Minimum temperature:", min_temp)
print("Maximum temperature:", max_temp)
print("Number of days with negative temperature:", negative_temp)
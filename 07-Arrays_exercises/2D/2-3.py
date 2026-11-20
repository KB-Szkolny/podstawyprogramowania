# Zadanie 2-3
# Wiersze: tygodnie 1-4 | Kolumny: [Food, Transport, Utilities][cite: 9]
monthly_expenses = [
    [200, 50, 100],  # Week 1[cite: 9]
    [180, 60, 110],  # Week 2[cite: 9]
    [220, 55, 105],  # Week 3[cite: 9]
    [210, 65, 95]    # Week 4[cite: 9]
]

food_total = 0
transport_total = 0
utilities_total = 0
weekly_totals = []

for week in monthly_expenses:
    food_total += week[0]
    transport_total += week[1]
    utilities_total += week[2]
    weekly_totals.append(sum(week))

total_month = sum(weekly_totals)

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
for idx, w_total in enumerate(weekly_totals, start=1):
    print(f'Week {idx}:', w_total)
print('----------------')
print('TOTAL:', total_month)
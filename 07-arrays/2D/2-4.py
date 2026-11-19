# Zadanie 2-4
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

def day_meal_plan(meal_plan, day_number):
    # Łączymy posiłki danego dnia w jeden tekst rozdzielony przecinkami[cite: 10]
    return ", ".join(meal_plan[day_number - 1])

print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")

for day in range(1, 8):
    print(f"{weekday(day)}: {day_meal_plan(meal_plan, day)}")
# Zadanie 1-16
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
              "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

# Sortowanie rosnąco (od najmniejszej do największej wartości)[cite: 7]
print("Distances (ascending):", sorted(distances_traveled))

# Sortowanie malejąco (od najwyższej do najniższej wartości)[cite: 7]
print("Temperatures (descending):", sorted(daily_temperatures, reverse=True))

# Sortowanie alfabetyczne nazw plików[cite: 7]
print("Files (ascending):", sorted(file_names))
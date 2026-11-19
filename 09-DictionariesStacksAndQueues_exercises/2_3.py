def main():
    # Zbiory wszystkich zapisanych oraz obecnych studentów
    all_students = {"Alice", "John", "Sara", "Bob"}
    attended_students = {"Alice", "Bob"}

    # Różnica zbiorów (-) zwraca osoby, które są w all_students, ale nie ma ich w attended_students
    absent_students = all_students - attended_students

    # Wyświetlenie zbioru nieobecnych studentów
    print(absent_students)

if __name__ == "__main__":
    main()
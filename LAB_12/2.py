#Ә тапсырмасы
grades = []

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name,score = line.strip().split(",")
        grades.append(int(score))

count = len(grades)
total = sum(grades)
average = total / count if count > 0 else 0

with open("report.txt", "w", encoding="utf-8") as file:
    file.write(f"Студент саны: {count}\n")
    file.write(f"Жалпы балл: {total}\n")
    file.write(f"Орташа балл: {average}\n")

print("Есеп report.txt файлына сақталды.")

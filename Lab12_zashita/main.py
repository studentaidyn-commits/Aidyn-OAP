#1 нұсқа
import json

students = []
grades = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line == "":
            continue

        try:
            name, grade_text = line.split(",")
            grade = int(grade_text)

            if grade < 0 or grade > 100:
                print("Қате баға:", line)
                continue

            student = {
                "name": name,
                "grade": grade
            }

            students.append(student)
            grades.append(grade)

        except ValueError:
            print("Қате формат:", line)

average = sum(grades) / len(grades) if grades else 0

count = 0

for grade in grades:
    if grade > 50:
        count += 1

with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Студент саны: " + str(len(students)) + "\n")
    file.write("Орташа баға: " + str(round(average, 1)) + "\n")
    file.write("50-ден жоғары алғандар саны: " + str(count))

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as file:
    restored = json.load(file)

print("Студенттер:", restored)
print("Жазбалар саны:", len(restored))
print("Бірінші студент:", restored[0]["name"])

print("Деректер сәйкес:", students == restored)

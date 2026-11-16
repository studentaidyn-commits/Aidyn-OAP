#В тапсырмасы
students = []
with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        try:
            name, grade = line.split(",")
            grade = int(grade)

            students.append({
                "name": name,
                "grade": grade
            })

        except ValueError:
            print("Қате формат! Жол өткізілді:", line)

print("\nДұрыс жазбалар:")

for student in students:
    print(student["name"], "-", student["grade"])

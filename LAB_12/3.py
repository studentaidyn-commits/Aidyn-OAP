#Б тапсырмасы
import json

students = [
    {"name": "Айдана", "grade": 85},
    {"name": "Ержан", "grade": 72},
    {"name": "Мадина", "grade": 94},
    {"name": "Али", "grade": 80},
    {"name": "Дана", "grade": 90}
]

# JSON файлына сақтау
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

# JSON файлынан қайта оқу
with open("data.json", "r", encoding="utf-8") as file:
    restored = json.load(file)

# Деректерді салыстыру
if students == restored:
    print("Деректер бастапқы мәліметтермен сәйкес келеді!")
else:
    print("Деректер сәйкес келмейді!")

print("Жазбалар саны:", len(restored))
print("Бірінші студент:", restored[0]["name"])

#А тапсырмасы
with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

non_empty = 0
total_words = 0

for line in lines:
    if line.strip():
        non_empty += 1
        total_words += len(line.split())

print("Бос емес жолдар саны:", non_empty)
print("Барлық сөздер саны:", total_words)
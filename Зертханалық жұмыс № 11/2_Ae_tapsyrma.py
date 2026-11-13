# Ә тапсырмасы
genres = [
    "Фантастика", "Роман", "Детектив", "Фантастика",
    "Поэзия", "Роман", "Тарихи", "Детектив",
    "Фантастика", "Комедия", "Роман", "Тарихи"
]

frequency = {}

for genre in genres:
    if genre in frequency:
        frequency[genre] += 1
    else:
        frequency[genre] = 1

print("Жанрлардың жиілігі:")
for genre, count in frequency.items():
    print(genre, "-", count)

max_count = max(frequency.values())
print("Ең жиі кездесетін жанр(лар):")

for genre, count in frequency.items():
    if count == max_count:
        print(genre, "-", count)

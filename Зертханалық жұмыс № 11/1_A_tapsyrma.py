# А тапсырмасы
genres = [
    "Фантастика", "Роман", "Детектив", "Фантастика",
    "Поэзия", "Роман", "Тарихи", "Детектив",
    "Фантастика", "Комедия", "Роман", "Тарихи"
]
unique_genres = set(genres)
duplicate_count = len(genres) - len(unique_genres)
print("Кітап жанрлары:", genres)
print("Бірегей жанрлар:", unique_genres)
print("Бірегей жанрлар саны:", len(unique_genres))
print("Қайталанатын элементтер саны:", duplicate_count)

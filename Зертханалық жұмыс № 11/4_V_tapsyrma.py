# В тапсырмасы
def check_genres(genres):
    print("\nБастапқы тізім:", genres)

    if len(genres) == 0:
        print("Тізім бос.")
        print("Бірегей элементтер: set()")
        print("Қайталанатын элементтер саны: 0")
        return

    unique_genres = set(genres)
    duplicate_count = len(genres) - len(unique_genres)

    frequency = {}
    for genre in genres:
        if genre in frequency:
            frequency[genre] += 1
        else:
            frequency[genre] = 1

    print("Бірегей жанрлар:", unique_genres)
    print("Қайталанатын элементтер саны:", duplicate_count)
    print("Жиілігі:", frequency)

    max_count = max(frequency.values())
    print("Ең жиі кездесетін мән(дер):")
    for genre, count in frequency.items():
        if count == max_count:
            print(genre, "-", count)



print("1-тест: Бос тізім")
check_genres([])

print("\n2-тест: Қайталанусыз тізім")
check_genres(["Роман", "Поэзия", "Детектив"])

print("\n3-тест: Барлық мәндері бірдей")
check_genres(["Фантастика", "Фантастика", "Фантастика", "Фантастика"])

print("\n4-тест: Қайталанатын жанрлар бар")
check_genres(["Роман", "Фантастика", "Роман", "Детектив", "Роман"])

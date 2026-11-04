text = input("Мәтінді енгізіңіз: ")

while True:
    print("Мәтін")
    print("1. Find")
    print("2. Replace")
    print("3. Мәтінді ауысыру")
    print("4. Кодты тексеру")
    print("5. Exit")

    choice = input("Таңдауыңызды енгізіңіз (1-5): ")

    if choice == "1":
        search_word = input("Іздеу сөзін енгізіңіз: ")

        if search_word.lower() in text.lower():
            print("Іздеу сөзі табылды:", search_word)
        else:
            print("Іздеу сөзі табылмады")
            
    elif choice == "2":
        old_word = input("Алмастырылатын сөз: ")
        new_word = input("Жаңа сөз: ")

        if old_word in text:
            text = text.replace(old_word, new_word)
            print("Жаңа мәтін:", text)
        else:
            print("Сөз мәтіннен табылмады")

    elif choice == "3":
        print("Ағымдағы мәтін:", text)
        answer = input("Мәтінді өзгертесіз бе? (Y/N): ")

        if answer.lower() == "y":
            text = input("Жаңа мәтінді енгізіңіз: ")
            print("Мәтін өзгертілді.")
        else:
            print("Мәтін сақталды.")

    elif choice == "4":
        value = input("Кодты енгізіңіз (GH-012): ").strip()

        valid = (
            len(value) == 6
            and value[:2].isalpha()
            and value[:2].isupper()
            and value[2] == "-"
            and value[3:].isdigit()
        )

        if value == "GH-012" and valid:
            print("Код дұрыс!")
        else:
            print("Қате код!")

    elif choice == "5":
        print("Бағдарлама аяқталды.")
        break

    else:
        print("Қате таңдау! Қайта енгізіңіз.")
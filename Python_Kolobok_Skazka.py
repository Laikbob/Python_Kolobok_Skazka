#Kolobok
heroes = ["Заяц", "Волк", "Медведь", "Лиса"]

for hero in heroes:
    print(f"{hero}: Колобок, я тебя съем!")
    if hero == "Лиса":
        print("Колобок спел песенку и попался Лисе. Его съели!")
        break
    else:
        print("Колобок: Я от тебя уйду!")

#Nädala päevad
def get_weekday(day):
    days = {
        1: "Esmaspäev (Понедельник)",
        2: "Teisipäev (Вторник)",
        3: "Kolmapäev (Среда)",
        4: "Neljapäev (Четверг)",
        5: "Reede (Пятница)",
        6: "Laupäev (Суббота)",
        7: "Pühapäev (Воскресенье)"
    }
    return days.get(day, "Неверный номер дня недели")


while True:
    print("Введите номер дня недели (1-7) или 0 для выхода.")
    try:
        day_number = int(input("Ваш выбор: "))
        if day_number == 0:
            print("Программа завершена.")
            break
        print(get_weekday(day_number))
    except ValueError:
        print("Пожалуйста, введите корректное число.")

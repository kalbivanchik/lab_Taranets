#Здесь хранятся и данные (состояние игры), и правила (описание, перемещение, случайности).
#Импортируем random для генерации случайных чисел.
import random

#СОСТОЯНИЕ ИГРЫ

#Текущая комната игрока. Старт — "hall" (по ТЗ).
room = "hall"

#Счетчик собранных улик. Начинается с нуля.
clues = 0

#Флаг наличия ключа. False — ключа нет.
has_key = False

#Флаг работы игры. Пока True, главный цикл в main.py работает.
game_running = True

#Значение для random.seed — фиксируем, чтобы события были воспроизводимы при отладке.
#Число 42 — отсылка к "Автостопом по галактике", негласный стандарт в IT.
SEED_VALUE = 42


def describe(current_room):
    #Сравниваем комнату с известными через if/elif (списки запрещены).
    if current_room == "hall":
        return "Холл: пыльный вестибюль с портретом хозяина. Выходы: north (библиотека), east (кабинет)."
    elif current_room == "library":
        return "Библиотека: стеллажи до потолка. Выход: south (холл)."
    elif current_room == "study":
        return "Кабинет: массивный стол, сейф и тяжёлая дверь, вы видите ключ на столе. Выходы: west (холл), north (спальня), east (подвал), door (выход)."
    elif current_room == "bedroom":
        return "Спальня: смятая кровать. Выходы: south (кабинет), north (чердак)."
    elif current_room == "basement":
        return "Подвал: сырость и паутина. Выход: west (кабинет)."
    elif current_room == "attic":
        return "Чердак: старые сундуки и пыль. Выход: south (спальня)."
    elif current_room == "exit":
        return "Выход: тяжёлая дубовая дверь. Она заперта на ключ."
    else:
        #Если пришло неизвестное имя комнаты
        return "Неизвестная комната."


def move(current_room, direction):
    #ХОЛЛ
    if current_room == "hall":
        if direction == "north": return "library"
        if direction == "east":  return "study"
    #БИБЛИОТЕКА
    elif current_room == "library":
        if direction == "south": return "hall"
    #КАБИНЕТ
    elif current_room == "study":
        if direction == "west":  return "hall"
        if direction == "north": return "bedroom"
        if direction == "east":  return "basement"
        if direction == "door":  return "exit"
    #СПАЛЬНЯ
    elif current_room == "bedroom":
        if direction == "south": return "study"
        if direction == "north": return "attic"
    #ПОДВАЛ
    elif current_room == "basement":
        if direction == "west":  return "study"
    #ЧЕРДАК
    elif current_room == "attic":
        if direction == "south": return "bedroom"
    #ВЫХОД
    elif current_room == "exit":
        if direction == "in":    return "study"
    #Если ни одно правило не сработало — игрок остаётся на месте
    return current_room


def random_clue():
    #Бросаем число от 1 до 5 (5 видов улик)
    number = random.randint(1, 5)
    #Через if/elif возвращаем нужную строку
    if number == 1:
        return "старое письмо"
    elif number == 2:
        return "обрывок карты"
    elif number == 3:
        return "засохшая роза"
    elif number == 4:
        return "сломанные часы"
    else:
        return "пятно на ковре"


def random_event():
    #Бросаем число от 1 до 3 (ровно 3 события)
    number = random.randint(1, 3)
    #Через if/elif выбираем строку (без списков)
    if number == 1:
        return "Скрип половиц раздался за спиной..."
    elif number == 2:
        return "Где-то хлопнула дверь!"
    else:
        return "Вы заметили найденное письмо на полу."
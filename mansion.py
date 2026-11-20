#МОДУЛЬ ОСОБНЯКА
import random
#Устанавливаем seed
SEED_VALUE = 42
random.seed(SEED_VALUE)
#1. Словарь описаний комнат
ROOM_DESCRIPTIONS = {
    "hall": "Холл: пыльный вестибюль с портретом хозяина.",
    "library": "Библиотека: стеллажи до потолка.",
    "study": "Кабинет: массивный стол и сейф. Может в сейфе есть ключ?",
    "bedroom": "Спальня: смятая кровать.",
    "basement": "Подвал: сырость и паутина.",
    "attic": "Чердак: старые сундуки.",
    "exit": "Выход: тяжёлая дубовая дверь."
}
#2. Словарь правил перемещения(направление -> комната)
ROOM_MOVES = {
    "hall": {"north": "library", "east": "study"},
    "library": {"south": "hall"},
    "study": {"west": "hall", "north": "bedroom", "east": "basement", "door": "exit"},
    "bedroom": {"south": "study", "north": "attic"},
    "basement": {"west": "study"},
    "attic": {"south": "bedroom"},
    "exit": {"in": "study"}
}

#3. Множество посещённых комнат(для проверки, осматривали ли мы уже комнату)
visited_rooms = set()
#4. Список для хранения собранных улик
clues = []
#5. Флаг наличия ключа
has_key = False
def add_clue(clues_list, c):
#Функция add_clue(clues, c) — добавляет улику в список. Возвращает обновленный список.
    #Добавляем улику(строку) в список
    clues_list.append(c)
    #Возвращаем список
    return clues_list


def count_clues(clues_list):
    #Функция count_clues(clues) — возвращает количество улик.
    #Возвращаем длину списка
    return len(clues_list)


def describe(room):
    #Функция describe(room) — возвращает описание комнаты из словаря.
    #Метод .get() безопасно достает значение. Если ключа нет, вернет строку по умолчанию.
    return ROOM_DESCRIPTIONS.get(room, "Неизвестная комната.")


def move(current_room, direction):
    #Функция move(room, direction) — возвращает новую комнату.
    #Проверяем, есть ли текущая комната в словаре переходов
    if current_room in ROOM_MOVES:
        #Если есть, ищем направление в ее внутреннем словаре
        #Если направления нет, возвращаем текущую комнату
        return ROOM_MOVES[current_room].get(direction, current_room)

    #Если комнаты вообще нет в словаре(защита от ошибок)
    return current_room


def random_clue():
    #Функция random_clue() — возвращает случайную улику.Теперь используем random.choice.
    #Список возможных улик
    possible_clues = ["старое письмо", "обрывок карты", "засохшая роза", "сломанные часы", "пятно на ковре"]
    #random.choice выбирает случайный элемент из списка
    return random.choice(possible_clues)


def random_event():
    #Функция random_event() — возвращает строку случайного события.
    #Список событий
    events = ["Скрип половиц раздался за спиной...", "Где-то хлопнула дверь!", "Вы заметили найденное письмо на полу."]
    #Возвращаем случайное
    return random.choice(events)


#НОВЫЕ ФУНКЦИИ-ГЕНЕРАТОРЫ
def get_long_clues(clues_list):
    #Фильтруем улики длиннее 5 символов.
    #Генераторное выражение: берем c из списка, если длина строки > 5
    return (c for c in clues_list if len(c) > 5)


def format_clues(clues_list):
    #форматируем улики, добавляя префикс.
    #Возвращаем отформатированные строки
    return (f"Улика: {c}" for c in clues_list)
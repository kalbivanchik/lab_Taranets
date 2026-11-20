#ГЛАВНЫЙ МОДУЛЬ ИГРЫ
import random
import mansion
from mansion import has_key
#Инициализация начального состояния
#Списки и множества в mansion.py уже созданы при импорте
current_room = "hall"
game_running = True
def show_help():
    #Функция show_help() — выводит список команд
    print("-" * 45)
    print("Доступные команды:")
    print("  help              - показать это сообщение")
    print("  look              - осмотреть комнату")
    print("  go <направление>  - перейти (north/south/east/west)")
    print("  door              - войти в дверь (в кабинете)")
    print("  take key          - взять ключ (в кабинете)")
    print("  clues             - показать количество улик")
    print("  long clues        - показать улики длиннее 5 символов (генератор)")
    print("  format clues      - показать красиво отформатированные улики (генератор)")
    print("  exit              - попытаться выйти из особняка")
    print("-" * 45)


def handle_look():
    #Функция осмотра
    #Получаем описание из mansion
    print(mansion.describe(current_room))
    #Если комнату еще не осматривали (её нет в множестве visited_rooms)
    if current_room not in mansion.visited_rooms:
        #Добавляем комнату в множество
        mansion.visited_rooms.add(current_room)
        #Шанс найти улику
        if random.randint(1, 10) == 1:
            #Получаем случайную улику
            c = mansion.random_clue()
            #Добавляем её через обязательную функцию add_clue
            mansion.add_clue(mansion.clues, c)
            print(f"Вы нашли улику: {c}! (+1 улика)")
        else:
            print("Вы ничего нового не обнаружили")
    else:
        print("Вы уже осматривали эту комнату")


def handle_move(direction):
    #Функция перемещения
    global current_room
    global has_key  #Нужен глобальный доступ, если мы меняем ключ, но здесь мы его не меняем
    #Получаем новую комнату через функцию move
    new_room = mansion.move(current_room, direction)
    #Если комната не изменилась
    if new_room == current_room:
        print("Туда идти нельзя")
        return
    #Обновляем текущую комнату
    current_room = new_room
    print(f"Вы перешли в: {current_room}")
    #Случайное событие
    event = mansion.random_event()
    print(f"Событие: {event}")
    #Если событие - письмо, добавляем улику
    if "письмо" in event:
        mansion.add_clue(mansion.clues, "найденное письмо")
        print("Вы подобрали письмо! (+1 улика)")


def handle_take_key(has_key):
    #Взятие ключа
    if current_room == "study":
        if not has_key:
            print("Вы взяли ключ из ящика стола!")
            return True
        else:
            print("Ключ уже у вас")
            return True
    else:
        print("Здесь нет ключа")
        return False




def handle_exit():
    #Проверка выхода
    global game_running
    if current_room == "exit" and has_key:
        print("\nВы вставили ключ в замок, дверь со скрипом открылась...")
        print("Вы выбрались из особняка! Победа!")
        game_running = False
    elif current_room == "exit" and not has_key:
        print("Дверь заперта! Нужен ключ.")
    else:
        print("Здесь нет выхода. Выход за дверью в кабинете")


#ЗАПУСК ИГРЫ
print("Добро пожаловать в Таинственный особняк!")
print("Введите 'help' для списка команд")
while game_running:
    print(f"\n[Комната: {current_room}]")
    user_input = input("> ").strip().lower()
    if user_input == "":
        continue
    elif user_input == "help":
        show_help()
    elif user_input == "look":
        handle_look()
    elif user_input.startswith("go "):
        direction = user_input[3:].strip()
        handle_move(direction)
    elif user_input == "door":
        if current_room == "study":
            handle_move("door")
        else:
            print("Здесь нет двери")
    elif user_input == "take key":
        has_key = handle_take_key(has_key)

        #ИСПОЛЬЗОВАНИЕ ГЕНЕРАТОРОВ
    elif user_input == "clues":
        #Выводим количество через функцию count_clues
        print(f"Всего улик: {mansion.count_clues(mansion.clues)}")
        print(f"Содержимое: {mansion.clues}")
    elif user_input == "long clues":
        #Используем генератор get_long_clues и превращаем его в список для вывода
        long_clues = list(mansion.get_long_clues(mansion.clues))
        print(f"Улики длиннее 5 символов: {long_clues}")
    elif user_input == "format clues":
        #Используем генератор format_clues
        formatted = list(mansion.format_clues(mansion.clues))
        print(f"Отформатированные улики: {formatted}")
    elif user_input == "exit":
        handle_exit()
    else:
        print("Неизвестная команда. Введите 'help'")
#ГЛАВНЫЙ МОДУЛЬ ИГРЫ
#Здесь цикл, обработка команд и обёртки над функциями модуля mansion.

#Импортируем random для установки seed
import random
#Импортируем наш единственный модуль с данными и правилами
import mansion

#Устанавливаем seed из mansion.SEED_VALUE, чтобы случайные события были воспроизводимы.
random.seed(mansion.SEED_VALUE)


def show_help():
    print("-" * 45)
    print("Доступные команды:")
    print("  help              - показать это сообщение")
    print("  look              - осмотреть комнату (шанс найти улику)")
    print("  go <направление>  - перейти (north/south/east/west)")
    print("  door              - войти в дверь (только в кабинете)")
    print("  take key          - взять ключ (только в кабинете)")
    print("  clues             - показать количество улик")
    print("  exit              - попытаться выйти из особняка")
    print("-" * 45)


def describe():
    #Передаём текущую комнату в mansion.describe и печатаем результат
    print(mansion.describe(mansion.room))


def move(direction):
    #Вызываем mansion.move, передавая текущую комнату и направление
    new_room = mansion.move(mansion.room, direction)

    #Если комната не изменилась — ход невозможен, выходим из функции
    if new_room == mansion.room:
        print("Туда идти нельзя (нет выхода в этом направлении).")
        return

    #Если комната изменилась — обновляем переменную room В МОДУЛЕ mansion
    mansion.room = new_room
    print(f"Вы перешли в: {mansion.room}.")

    #Разыгрываем случайное событие через mansion.random_event()
    event = mansion.random_event()
    print(f"Событие: {event}")

    #Если событие — "найденное письмо", добавляем улику в счётчик mansion.clues
    if "найденное письмо" in event:
        mansion.clues += 1
        print("Вы подобрали письмо! (+1 улика)")


def handle_look():
    describe()  #Сначала печатаем описание комнаты
    #Бросаем число от 1 до 3 — шанс найти улику
    chance = random.randint(1, 3)

    #Если выпало 1 — находим случайную улику через mansion.random_clue()
    if chance == 1:
        clue_name = mansion.random_clue()  #Получаем название улики
        mansion.clues += 1  #Увеличиваем счётчик в mansion
        print(f"Вы нашли улику: {clue_name}! (+1 улика)")
    else:
        print("Вы ничего нового не обнаружили.")


def handle_take_key():
    #Проверяем комнату через mansion.room
    if mansion.room == "study":
        #Проверяем флаг has_key в mansion
        if mansion.has_key == False:
            mansion.has_key = True  #Ставим флаг
            print("Вы взяли ключ из ящика стола!")
        else:
            print("Ключ уже у вас.")
    else:
        print("Здесь нет ключа.")


def handle_exit():
    #Проверяем оба условия (мы в exit И есть ключ)
    if mansion.room == "exit" and mansion.has_key == True:
        print("\nВы вставили ключ в замок, дверь со скрипом открылась...")
        print("Вы выбрались из особняка! Победа!")
        mansion.game_running = False  #Останавливаем игру
    elif mansion.room == "exit" and mansion.has_key == False:
        print("Дверь заперта! Нужен ключ.")
    else:
        print("Здесь нет выхода. Выход находится за дверью в кабинете (команда 'door').")

#БЛОК ЗАПУСКА
print("Добро пожаловать в Таинственный особняк!")
print("Цель: соберите улики, найдите ключ и выйдите.")
print("Введите 'help' для списка команд.")

#Главный цикл. Крутится, пока mansion.game_running == True
while mansion.game_running:
    #Показываем текущую комнату (берём из mansion.room)
    print(f"\n[Комната: {mansion.room}]")

    #Получаем команду: strip — убрать пробелы, lower — привести к нижнему регистру
    user_input = input("> ").strip().lower()

    #Пустая строка — пропускаем итерацию
    if user_input == "":
        continue

    #help — вызвать функцию show_help()
    elif user_input == "help":
        show_help()

    #look — осмотр комнаты
    elif user_input == "look":
        handle_look()

    #go <направление>: проверяем, что строка начинается с "go "
    elif user_input.startswith("go "):
        #Отрезаем "go " срезом [3:] и убираем лишние пробелы (без .split(), чтобы не создавать список)
        direction = user_input[3:].strip()
        move(direction)  #Передаём направление в функцию move

    #door — переход из кабинета в комнату exit
    elif user_input == "door":
        if mansion.room == "study":
            move("door")  #Используем move с направлением "door"
        else:
            print("Здесь нет двери.")

    #take key — взять ключ
    elif user_input == "take key":
        handle_take_key()

    #clues — вывести счётчик улик из mansion
    elif user_input == "clues":
        print(f"Собрано улик: {mansion.clues}")

    #exit — попытка выхода
    elif user_input == "exit":
        handle_exit()

    #Любая другая команда
    else:
        print("Неизвестная команда. Введите 'help'.")
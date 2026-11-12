#По заданию room, старт - "hall"
room = "hall"
#По заданию переменная clues = 0
clues = 0
#По заданию флаг has_key = False
has_key = False
#Техническая переменная для управления циклом игры
game_running = True
#Изначально улики не найдены(False). Это защитит от повторного счета
clues_library_found = False
clues_study_found = False
clues_bedroom_found = False
clues_basement_found = False
clues_attic_found = False
#По заданию Приветствие и цель
print("ДОБРО ПОЖАЛОВАТЬ В ТАИНСТВЕННЫЙ ОСОБНЯК")
print("ЦЕЛЬ:СОБЕРИТЕ УЛИКИ, НАЙДИТЕ КЛЮЧ И ПОКИНЬТЕ ОСОБНЯК")

while game_running:
    #Показываем игроку где он находится
    print(f"\n ВЫ НАХОДИТЕСЬ В КОМНАТЕ {room}")
    #Считываем комманды,убираем пробелы и приводим к нижнему регистру
    command = input("ВВЕДИТЕ КОМАНДУ : help, look, go, take, use, clues, exit ").strip().lower()
    #Блок обработки команды help
    if command == "help":
        print("Доступные команды")
        print(" help - показать это сообщение")
        print(" rooms digit - показать комнаты куда можно пойти")
        print(" look - осмотреть комнату")
        print(" go [комната] - перейти в другую комнату")
        print(" take [предмет] - взять предмет")
        print(" use [предмет] - использовать предмет")
        print(" clues - показать кол-во собранных улик")
        print(" exit - покинуть игру")
        print(" to exit - выйти из особняка(если есть ключ и находитесь в комнате 'exit)")

    #Блок обработки команды rooms digit(список всех доступных комнат)
    elif command == "rooms digit":
           print("доступные комнаты - hall, study, attic, bedroom, basement, exit, library")

    #Блок обработки команды exit(выход из игры)
    elif command == "exit":
        game_running = False
    #Блок обработки команды look
    elif command == "look":
        print(f"Вы осматриваете {room}...")
        #Если мы в комнате и улика там еще не была найдена:
        if room == "library" and clues_library_found == False:
            clues += 1
            clues_library_found = True#Меняем флаг на True чтобы больше не считать
            print("Вы нашли улику! Счетчик улик увеличен.")
        elif room == "study" and clues_study_found == False:
            clues += 1
            clues_study_found = True
            print("Вы нашли улику! Счетчик улик увеличен")
        elif room == "bedroom" and clues_bedroom_found == False:
                    clues += 1
                    clues_bedroom_found = True
                    print("Вы нашли улику! Счетчик улик увеличен")
        elif room == "basement" and clues_basement_found == False:
                    clues += 1
                    clues_basement_found = True
                    print("Вы нашли улику! Счетчик улик увеличен")
        elif room == "attic" and clues_attic_found == False:
                    clues += 1
                    clues_attic_found = True
                    print("Вы нашли улику! Счетчик улик увеличен")
        #Если ни одно условие выше не выполнилось, значит либо здесь нет улик, либо мы их уже забрали
        else:
               print("Здесь больше нет ничего интересного.")
        #Подсказки для игрока
        if room == "study":
               print("Вы видете ключ на столе.(Используйте 'take key')")
        elif room == "exit":
               print("Это выход из особняка.")
        else:
               print("Комната выглядит обычно.")
    #Блок обработки команды go
    elif command.startswith("go"):
           parts = command.split()#Разбиваем строку "go hall" на список ["go", "hall"]
           if len(parts) < 2:
                  print("Куда идти? Укажите комнату: go [название]")
           else:
                  target = parts[1]#Берем название комнаты
                  #Проверяем существует ли такая кмоната
                  #Здесь использование or заменяет проверку массива
                  if target == "hall" or target == "library" or target == "study" or target == "bedroom" or target == "basement" or target == "attic" or target == "exit":
                         room = target#Меняем текущую локацию
                         print(f"Вы перешли в {room}")
                  else:
                         print("Такой комнаты нет.")
    #Блок обработки команды take
    elif command == "take key":
           #Так как ключ можно взять только в комнате study
           if room == "study":
                  if not has_key:
                         has_key = True
                         print("Вы взяли ключ!")
                  else:
                         print("Ключ уже у вас.")
           else:
                  print("Здесь нет ключа.")
    #Блок обработки кмоанды use
    elif command == "use key":
           if room == 'exit':
                  if has_key:
                         print("Вы используете ключ и открываете дверь...")
                  else:
                         print("Здесь нечего открывать ключом.")
    #Блок обработки команды clues
    elif command == 'clues':
           print(f"Собрано улик: {clues}")
    #Блок обработки команды to exit
    elif command == 'to exit':
        #Победа: у exit при has_key == True
           if room == "exit" and has_key:
                  print("\nПоздравляем! Вы нашли ключ, собрали улики и выбрались из особняка!")
                  game_running = False
           elif room == "exit" and not has_key:
                  print("Дверь заперта. Необходимо найти ключ.")
           else:
                  print("Чтобы выйти из игры, вы должны находиться в комнате 'exit' с ключом")
    #Блок обработки неизвсетных команд
    else:
           print("Неизвестная команда. Введите 'help' для списка комманд.")
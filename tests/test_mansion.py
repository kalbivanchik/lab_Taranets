#ТЕСТЫ ДЛЯ МОДУЛЯ MANSION
#Импортируем наш модуль
import mansion
#ТЕСТЫ ДЛЯ ФУНКЦИЙ
def test_add_clue():
    #Тест функции add_clue
    #Создаем пустой тестовый список
    test_list = []
    #Вызываем функцию
    result = mansion.add_clue(test_list, "тестовая улика")
    #Проверяем, что улика добавилась
    assert len(result) == 1
    assert result[0] == "тестовая улика"

def test_count_clues():
    #Тест функции count_clues
    #Создаем тестовый список
    test_list = ["улика 1", "улика 2", "улика 3"]
    #Проверяем, что функция возвращает правильное число
    assert mansion.count_clues(test_list) == 3
    #Проверяем пустой список
    assert mansion.count_clues([]) == 0

def test_describe():
    #Тест функции describe
    #Проверяем, что для известной комнаты возвращается правильный текст
    assert "Холл" in mansion.describe("hall")
    #Проверяем, что для неизвестной комнаты возвращается заглушка
    assert mansion.describe("unknown") == "Неизвестная комната."

#ТЕСТЫ ДЛЯ ГЕНЕРАТОРОВ
def test_long_clues():
    #Тест генератора фильтрации улик длиннее 5 символов
    #Готовим список, где одни строки короче 5, другие длиннее
    clues = ["карта", "письмо", "роза", "часы", "отпечаток"]
    #Преобразуем генератор в список для сравнения
    result = list(mansion.get_long_clues(clues))
    #"карта" (5) - не пройдет, "письмо" (6) - пройдет
    assert result == ["письмо", "отпечаток"]

def test_format_clues():
    #Тест генератора форматирования
    clues = ["улика 1", "улика 2"]
    #Преобразуем генератор в список
    result = list(mansion.format_clues(clues))
    #Проверяем префикс
    assert result == ["Улика: улика 1", "Улика: улика 2"]

#ТЕСТ ДЛЯ СЛОВАРЕЙ И МНОЖЕСТВ
def test_move_dictionary():
    #Тест перемещения на основе словаря
    #Идем из холла на север должны попасть в библиотеку
    assert mansion.move("hall", "north") == "library"
    #Идем в неверном направлении остаемся в холле
    assert mansion.move("hall", "south") == "hall"
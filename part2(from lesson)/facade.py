from adapter import Printer, CSVReader, JSONReader


class Facade:  # Скроем работу с различными адаптерами за фасадом
    def __init__(self):
        self.csv_reader = Printer(CSVReader())  # создаем адаптер для обработки CSV строк
        self.json_reader = Printer(JSONReader())  # создаем адаптер для обработки JSON строку
        self.csv_files = []
        self.lson_files = []

    def fill_with_CSV(self, *args):
        """наполняем данные CSV"""
        self.csv_files = args

    def fill_with_JSON(self, *args):
        """Наполняем данные JSON"""
        self.json_files = args

    def _csv_print(self):
        """Выводим на печать содержимое файлов CSV"""
        i = 1
        print("Выводим CSV содержимого")
        for csv in self.csv_files:
            print(f"Печать файла № {i}")
            self.csv_reader.print(csv)
            i += 1

    def _json_print(self):
        """Выводим на печать содержимое файлов JSON"""
        i = 1
        print("Вывод JSON содержимого")
        for jsn in self.json_files:
            print(f"Печать файла № {i}")
            self.json_reader.print(jsn)
            i += 1

    def print(self):
        self._csv_print()
        self._json_print()


CSV1 = "Название;Цвет;Вес\nКот;Редкий окрас (скумбрия на снегу);3\nПес;Черный;15\nЧерепашка;Серый;0.2"
CSV2 = "Название;Цвет;Вес\nТюлень;Серый(металлик);60\nМедведь (северный);Белый;450\nЧерепашка(морская);Болотного цвета;160"
CSV3 = "Название;Цвет;Вес\nЖираф;Пятнистый;800\nЛеопард;Тоже пятнистый;80\nСвинка (морская);Пестрая;0.2"
JSON1 = '{"items": [{"Название": "Медведь", "Цвет": "Бурый", "Вес": "150"}, {"Название": "лиса", "Цвет": "рыжий", "Вес": "12"}]}'
JSON2 = '{"items": [{"Название": "Заяц", "Цвет": "Серый", "Вес": "5"}, {"Название": "Волк", "Цвет": "серый", "Вес": "22"}]}'

facade = Facade()
facade.fill_with_CSV(CSV1, CSV2, CSV3)
facade.fill_with_JSON(JSON1, JSON2)
facade.print()

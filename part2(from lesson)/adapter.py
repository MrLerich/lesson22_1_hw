import json
from abc import ABC, abstractmethod

# наши примеры файлов
from typing import List, Tuple

CSV = "Название;Цвет;Вес\nКот;Редкий окрас (скумбрия на снегу);3\nПес;Черный;15\nЧерепашка;Серый;0.2"
JSON = '{"items": [{"Название": "Медведь", "Цвет": "Бурый", "Вес": "150"},{"Название": "Лиса", "Цвет": "рыжий",' \
       '"Вес": "7"}]} '


class Adapter(ABC):  # Интерфейс Адаптерами
    @abstractmethod
    def get_data(self, source):
        pass


class CSVReader(Adapter):  # Реализация Адаптера под CSV строки
    def get_data(self, source):
        lines = self._split_lines(source)  # Разделяем нашу строку на отдельные списки строк
        headers, data = self._split_header_with_data(lines)  # отделяем заголовки от данных
        return self._format_result(headers, data)  # Преобразуем данные в требуемый формат

    def _split_lines(self, source) -> List:
        return source.split('\n')

    def _split_header_with_data(self, lines) -> Tuple:
        return lines[0].split(';'), [x.split(';') for x in lines[1:]]

    def _format_result(self, headers, data) -> List:
        items = []
        for line in data:
            items.append(dict(zip(headers, line)))
        return items


class JSONReader(Adapter):  # Реализация Адаптера под JSON строки
    def get_data(self, source):
        return json.loads(source)["items"]


class Printer:  # Реализация некоего класса, который взаимодействует с различными типами входных данных
    def __init__(self, adapter: Adapter):
        self.adapter = adapter
        self.data = []

    def _get_data(self, source):  # Передает нашему адаптеру исходную настройку
        self.data = self.adapter.get_data(source)

    def print(self, source):
        self._get_data(source)
        for line in self.data:  # выводим на печать данные, преобразованные в заведомо валидный формат
            print(f'В наличии: {line["Название"]}. Окрас: {line["Цвет"]}. Масса: {line["Вес"]}')


csv_printer = Printer(adapter=CSVReader())
json_printer = Printer(adapter=JSONReader())

csv_printer.print(CSV)
json_printer.print(JSON)

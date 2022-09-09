import json
import datetime
from pprint import pprint


def wrapper(func):
    """Обёртыватель - создаем функцию,котрая в качестве аргумента принимает другую функцию"""
    def log_func(*args, **kwargs): #Обогощаем вывод данными по длине контента и временем выполнения функции
        start_time = datetime.datetime.now()        #начало работы
        result = func(*args, **kwargs)      #получение результата от функция
        length = len(json.dumps(result)) # длина полученного контента
        delta_time = datetime.datetime.now() - start_time   #время работы функция
        result["length"] = length   #обогащение длиной контента
        result["duration"] = delta_time #обогащение временем работы функция
        return result

    return log_func


@wrapper
def parse_json(string):
    return json.loads(string)

JSON1 = '{"items": [{"Название": "Медведь", "Цвет": "Бурый", "Вес": "150"}, {"Название": "лиса", "Цвет": "рыжий", "Вес": "12"}]}'
JSON2 = '{"items": [{"Название": "Заяц", "Цвет": "Серый", "Вес": "5"}, {"Название": "Волк", "Цвет": "серый", "Вес": "22"}]}'

pprint(parse_json(JSON1))
print("=================")
pprint(parse_json(JSON2))
import time
import datetime

class Cache(object):
    # тут будет храниться сам обЪект кеша, который будет или создан
    # или возвращаться при попытке создать новый экземпляр класса
    _instance = None
    # хранилище нашего кеша
    vault: dict = {}

    # как вы помните __new__ вызывается перед __init__ поэтому именно тут есть смысл
    # подменять возвращаемый объекта
    def __new__(cls, *args, **kwargs):
        #если  объект еще не создан
        if not cls._instance:
        #то мы создаем новый экземпляр класса передав ему классб и параметры инициализации
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance #возвращаем сохраненный объект

    def set_value(self, key, value):
        """Установить какое-либо значение по ключу"""
        self.vault[key] = value

    def get_value(self, key):
        """Получить какое-либо значение по ключу"""
        return self.vault[key]

    def check(self, key) -> bool:
        """Проверить, есть ли такой ключ в коллекции"""
        return key in self.vault


class Source:
    def get_something(self, key):
        """Метод заглушка ждет 5 сек и возвращает одну и ту же строку"""
        time.sleep(5)
        return 'result'


class App:
    def __init__(self):
        self.cache = Cache()    #при инициализации получаем экземпляр класса Cashe
        self.source = Source()  #при инициализации получаем экземпляр класс Source

    def process(self, key):
        start_time = datetime.datetime.now()    #время начала выполнения функция
        if self.cache.check(key):   #проверяем есть ли этот ключ в кеше
            result = self.cache.get_value(key)  #возвращаем значение из кеша
        else:
            result = self.source.get_something(key)     #получаем значение из источника
            self.cache.set_value(key, result)   #устанавливаем значение в кеш
        print(datetime.datetime.now() - start_time)     #выводим время работы функция
        return result


app = App()
app2 = App()

print("Являются ли эти два объекта одинаковыми: ", id(app) == id(app2))
print("Являются ли кеши одинаковыми: ", id(app.cache) == id(app2.cache))
print("Запустим выполнение в первый раз и получение данных из источника займет у нас около 5 секунд")

app.process(1)
print("При повторном выполнении данные будут получаться уже из кеша, и поэтому они будут получены почти мгновенно")

app.process(1)
print("Данные для другого источника по прежнему в первый раз будут получаться долго")

app2.process(2)
print("Поскольку у нас кеш у нас физически один на два разных объекта(хотя каждый из них создал для себя экземпляр "
      "самостоятельно) то второй объект уже не будет обращаться к источнику данных а возьмет их сразу из кеша")

app2.process(1)
print("Если мы выполним этот блок кода еще раз, то данные будут получены моментально, потому что не смотря на то что "
      "объекты app и app2 будут уже другими - кеш у них будет тот же самый")







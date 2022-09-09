# # Измените класс Person так, чтобы его методы
# # # оперировали внутренним состоянием,
# # # а не использовали цепочку вызовов объектов
# #
# # class Room:
# #     def get_name(self):
# #         return 42
# #
# #
# # class Street:
# #     def get_room(self) -> Room:
# #         return Room()
# #
# #
# # class City:
# #     def get_street(self) -> Street:
# #         return Street()
# #
# #     def population(self):
# #         return 100500
# #
# #
# # class Country:
# #     def get_city(self) -> City:
# #         return City()
# #
# #
# # class Planet:
# #     def get_contry(self) -> Country:
# #         return Country()
# #
# #
# # class Person:
# #     def __init__(self):
# #         self.planet = Planet()
# #
# #     def get_person_room(self):
# #         return self.planet.get_contry().get_city().get_street().get_room().get_name()
# #
# #     def get_city_population(self):
# #         return self.planet.get_contry().get_city().population()
# #
# #

# # # сделать экземпляр класса person и вызвать новые методы.
class Person:
    def __init__(self, city_population, room_num):
        self.city_popultaion = city_population
        self.room_num = room_num

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_popultaion

person = Person(100_000, 2)
print(f"room is {person.get_person_room()}")
print(f"population is {person.get_city_population()}")

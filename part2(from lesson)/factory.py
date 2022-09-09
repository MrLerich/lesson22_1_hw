from abc import ABC, abstractmethod

from pip._internal.resolution.resolvelib import factory


class AbstractCar(ABC):
    @abstractmethod
    def deliver_by_land(self):
        pass


class AbstractShip(ABC):
    @abstractmethod
    def deliver_by_sea(self):
        pass


class AbstractTransportFactory(ABC):
    @abstractmethod
    def create_car(self) -> AbstractCar:
        pass

    @abstractmethod
    def create_ship(self) -> AbstractShip:
        pass


class TeslaX(AbstractCar):
    def deliver_by_land(self):
        print("Быстро и стремительно коробочки помчались в путь")


class HeavyTruck(AbstractCar):
    def deliver_by_land(self):
        print("Медленно и печально контейнеровоз пытается вписаться в поворот")


class RubberBoat(AbstractShip):
    def deliver_by_sea(self):
        print("Радостно плюхая веслами гребцы выбираются из приливной волны")


class CargoShip(AbstractShip):
    def deliver_by_sea(self):
        print("Лихо и бесбашенно выписывают развороты в Суэцком канале")


class UsualTransportFactory(AbstractTransportFactory):
    def create_car(self) -> AbstractCar:
        return TeslaX()

    def create_ship(self) -> AbstractShip:
        return RubberBoat()


class CargoTransportFactory(AbstractTransportFactory):
    def create_car(self) -> AbstractCar:
        return HeavyTruck()

    def create_ship(self) -> AbstractShip:
        return CargoShip()


class Warehouse:
    factory: AbstractTransportFactory

    def __init__(self, factory: AbstractTransportFactory):
        self.factory = factory

    def deliver_with_ship(self):
        ship = self.factory.create_ship()
        ship.deliver_by_sea()

    def deliver_with_car(self):
        car = self.factory.create_car()
        car.deliver_by_land()


warehouse = Warehouse(factory=CargoTransportFactory())
warehouse.deliver_with_ship()
warehouse.deliver_with_car()

warehouse = Warehouse(factory=UsualTransportFactory())
warehouse.deliver_with_ship()
warehouse.deliver_with_car()

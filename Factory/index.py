from abc import ABCMeta, abstractmethod


class IBread(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def make_bread():
        pass


class Sourdough(IBread):
    def __init__(self, quantity):
        self.name = "Sourdough"
        self.quantity = quantity

    def make_bread(self):
        return 'Making {0} of {1}!'.format(self.quantity, self.name)


class Ciabatta(IBread):
    def __init__(self, quantity):
        self.name = "Ciabatta"
        self.quantity = quantity

    def make_bread(self):
        return 'Making {0} of {1}!'.format(self.quantity, self.name)


class BreadFactory:
    @ staticmethod
    def produce_bread(bread_type, quantity):
        if bread_type == 'Ciabatta':
            return Ciabatta(quantity)
        if bread_type == 'Sourdough':
            return Sourdough(quantity)
        return None


sourdough = BreadFactory().produce_bread('Sourdough', 5)
sourdough.make_bread()

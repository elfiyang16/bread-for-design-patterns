import abc


class BreadFlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_bread_flyweight(self, flour_kind, kind):
        try:
            flyweight = self._flyweights[kind]
        except KeyError:
            flyweight = ConcreteBreadFlyweight(flour_kind, kind)
            self._flyweights[kind] = flyweight
        return flyweight


class BreadFlyweightInterface(metaclass=abc.ABCMeta):
    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def wait_for_bake(self, extrinsic_state):
        pass

    @abc.abstractmethod
    def wait_for_fry(self, extrinsic_state):
        pass

    @abc.abstractmethod
    def wait_for_toast(self, extrinsic_state):
        pass


class ConcreteBreadFlyweight(BreadFlyweightInterface):
    def __init__(self, kind=None, flour_kind="white"):
        self.kind = kind
        self.flour_kind = flour_kind

    def wait_for_bake(self, min):
        return f"{self.kind} is waiting for bake in {min}!"

    def wait_for_fry(self, min):
        return f"{self.kind} is waiting for fry in {min}!"

    def wait_for_toast(self, min):
        return f"{self.kind} is waiting for toast in {min}!"


bread_factory = BreadFlyweightFactory()
sourdough = bread_factory.get_bread_flyweight("sourdough")
sourdough.wait_for_toast(30)

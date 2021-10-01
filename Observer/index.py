from abc import ABCMeta, abstractmethod


class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        pass

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        pass

    @staticmethod
    @abstractmethod
    def notify(observer):
        pass


class BreadObservable(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class LabelBreadObserver():
    def __init__(self, observable):
        observable.subscribe(self)

    def update(self, data):
        print(f"A bread marked as {data}")


class BakeBreadObserver():
    def __init__(self, observable):
        observable.subscribe(self)

    def update(self, data):
        print(f"A bread baked as {data}")


class WaitForRiseBreadObserver():
    def __init__(self, observable):
        observable.subscribe(self)

    def update(self, data):
        print(f"Waiting for {data} to rise")


breadObserver = BreadObservable()

labelBreadObserver = LabelBreadObserver(breadObserver)
bakeBreadObserver = BakeBreadObserver(breadObserver)

breadObserver.notify("Sourdough")

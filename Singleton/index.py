
import threading


class BreadSingleton:

    __instance = None

    def __init__(self):
        if BreadSingleton.__instance:
            raise Exception(
                "An instance already been initiated !")
        else:
            BreadSingleton.__instance = self

    def bake_bread(self, quantity, name):
        self.quantity = quantity
        self.name = name

    def put_on_shelf(self):
        print(f"{self.quantity} of {self.name} are put on shelf!")

    @staticmethod
    def getInstance():
        if not BreadSingleton.__instance:
            BreadSingleton()
        return BreadSingleton.__instance


oven1 = BreadSingleton.getInstance()
oven1.bake_bread(5, "sourDough")
oven1.put_on_shelf()

oven2 = BreadSingleton.getInstance()
oven2.bake_bread(10, "ciabatta")
oven2.put_on_shelf()

print(oven1 == oven2)


class BreadSingletonTwo:

    __singleton_lock = threading.Lock()
    __instance = None

    def __init__(self):
        if not BreadSingletonTwo.__instance:
            with BreadSingletonTwo.__singleton_lock:
                if not BreadSingletonTwo.__instance:
                    BreadSingletonTwo.__instance = self
        else:
            raise Exception(
                "An instance already been initiated !")

    def bake_bread(self, quantity, name):
        self.quantity = quantity
        self.name = name

    def put_on_shelf(self):
        print(f"{self.quantity} of {self.name} are put on shelf!")

    @staticmethod
    def get_instance():
        if not BreadSingletonTwo.__instance:
            BreadSingletonTwo()
        return BreadSingletonTwo.__instance

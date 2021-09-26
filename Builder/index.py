from abc import ABCMeta, abstractmethod


class IBread(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def label_bread(kind):
        "Bread kind"

    @staticmethod
    @abstractmethod
    def choose_flour(flour_kind):
        pass

    @staticmethod
    @abstractmethod
    def wait_for_rise(rise_in_min):
        pass

    @staticmethod
    @abstractmethod
    def wait_for_bake(bake_in_min, temp):
        pass

    @staticmethod
    @abstractmethod
    def get_result():
        pass


class Bread():
    def __init__(self, kind=None, flour_kind="white",
                 rise_in_min=0, bake_in_min=0, temp=200):
        self.kind = kind
        self.flour_kind = flour_kind
        self.rise_in_min = rise_in_min
        self.bake_in_min = bake_in_min
        self.temp = temp

    def who_am_i(self):
        return f"I am {self.kind} that is made of {self.flour_kind}"\
            f"and is baked under {self.temp} for {self.bake_in_min}!"


class BreadBuilder(IBread):
    def __init__(self):
        self.bread = Bread()

    def label_bread(self, kind):
        self.bread.kind = kind
        return self

    def choose_flour(self, flour_kind):
        self.bread.flour_kind = flour_kind
        return self

    def wait_for_rise(self, rise_in_min):
        self.bread.rise_in_min = rise_in_min
        return self

    def wait_for_bake(self, bake_in_min, temp):
        self.bread.bake_in_min = bake_in_min
        self.bread.temp = temp
        return self

    def get_result(self):
        return self.bread


class SourdoughDirector:
    @staticmethod
    def construct():
        return BreadBuilder()\
            .label_bread("Sourdough")\
            .choose_flour("Wholemeal")\
            .wait_for_rise(30)\
            .wait_for_bake(120, 200)\
            .get_result()


class CiabattaDirector:
    @staticmethod
    def construct():
        return BreadBuilder()\
            .label_bread("Ciabatta")\
            .choose_flour("Wholemeal")\
            .wait_for_rise(100)\
            .wait_for_bake(90, 220)\
            .get_result()


sourdough = SourdoughDirector.construct()

print(sourdough.who_am_i())

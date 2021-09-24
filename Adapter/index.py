import abc


class BreadAdapterInterface(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def labelBread(self, **args):
        pass

    @abc.abstractmethod
    def chooseFlour(self, **args):
        pass

    @abc.abstractmethod
    def waitForBake(self, **args):
        pass


class BreadAdaptee():
    def __init__(self, kind=None, flour_kind="white",
                 rise_in_min=0, bake_in_min=0, temp=200):
        self.kind = kind
        self.flour_kind = flour_kind
        self.rise_in_min = rise_in_min
        self.bake_in_min = bake_in_min
        self.temp = temp

    def label_bread(self, kind):
        self.kind = kind

    def choose_flour(self, flour_kind):
        self.flour_kind = flour_kind

    def wait_for_bake(self, bake_in_min, temp):
        self.bake_in_min = bake_in_min
        self.temp = temp


class BreadAdapter(BreadAdapterInterface):
    __bread = None

    def __init__(self, bread=BreadAdaptee()):
        self.__bread = bread

    def labelBread(self, **args):
        return self.__bread.label_bread(args)

    def chooseFlour(self, **args):
        return self.__bread.choose_flour(args)

    def waitForBake(self, **args):
        return self.__bread.wait_for_bake(args)


breadAdapter = BreadAdapter()
breadAdapter.chooseFlour("Wholemeal")

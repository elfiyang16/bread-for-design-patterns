class Oven:
    def wait_for_bake(self, bake_in_min):
        self.bake_in_min = bake_in_min


class Mixer:
    def choose_flour(self, flour_kind):
        self.flour_kind = flour_kind

    def wait_for_rise(self, rise_in_min):
        self.rise_in_min = rise_in_min


class Shelf:
    def label_bread(self):
        pass


class BreadFacade:
    def __init__(self):
        self.mixer = Mixer()
        self.oven = Oven()
        self.shelf = Shelf()

    def produce(self, flour_kind, rise_in_min, bake_in_min):
        self.mixer.choose_flour(flour_kind)
        self.mixer.wait_for_rise(rise_in_min)
        self.oven.wait_for_bake(bake_in_min)
        self.shelf.label_bread()


bread = BreadFacade()
bread.produce("wholemeal", 60, 120)

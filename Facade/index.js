class Oven {
  wait_for_bake(bake_in_min) {
    this.bake_in_min = bake_in_min;
    return;
  }
}

class Mixer {
  choose_flour(flour_kind) {
    this.flour_kind = flour_kind;
    return;
  }

  wait_for_rise(rise_in_min) {
    this.rise_in_min = rise_in_min;
    return;
  }
}

class Shelf {
  label_bread() {
    return;
  }
}

class BreadFacade {
  constructor() {
    this.mixer = new Mixer();
    this.oven = new Oven();
    this.shelf = new Shelf();
  }

  produce(flour_kind, rise_in_min, bake_in_min) {
    this.mixer.choose_flour(flour_kind);
    this.mixer.wait_for_rise(rise_in_min);
    this.oven.wait_for_bake(bake_in_min);
    this.shelf.label_bread();
  }
}

let bread = new BreadFacade();
bread.produce("wholemeal", 60, 120);

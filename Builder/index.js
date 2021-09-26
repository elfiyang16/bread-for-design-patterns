class Bread {
  constructor(
    kind = None,
    flour_kind = "white",
    rise_in_min = 0,
    bake_in_min = 0,
    temp = 200
  ) {
    this.kind = kind;
    this.flour_kind = flour_kind;
    this.rise_in_min = rise_in_min;
    this.bake_in_min = bake_in_min;
    this.temp = temp;
  }

  whoAmI() {
    return `I am ${this.kind} that is made of ${this.flour_kind} \n
           and is baked under ${this.temp} for ${this.bake_in_min}!`;
  }
}

class BreadBuilder {
  constructor() {
    this.bread = new Bread();
  }

  label_bread(kind) {
    this.bread.kind = kind;
    return this;
  }

  choose_flour(flour_kind) {
    this.bread.flour_kind = flour_kind;
    return this;
  }

  wait_for_rise(rise_in_min) {
    this.bread.rise_in_min = rise_in_min;
    return this;
  }

  wait_for_bake(bake_in_min, temp) {
    this.bread.bake_in_min = bake_in_min;
    this.bread.temp = temp;
    return this;
  }

  get_result() {
    return this.bread;
  }
}

class BreadDirector {
  constructor(builder = new BreadBuilder()) {
    this.builder = builder;
  }

  constructCiabatta() {
    return this.builder
      .label_bread("Ciabatta")
      .choose_flour("Wholemeal")
      .wait_for_rise(100)
      .wait_for_bake(90, 220)
      .get_result();
  }

  constructSourdougha() {
    return this.builder
      .label_bread("Sourdough")
      .choose_flour("Wholemeal")
      .wait_for_rise(30)
      .wait_for_bake(120, 200)
      .get_result();
  }
}

const sourdough = new BreadDirector().constructSourdougha();
sourdough.whoAmI();

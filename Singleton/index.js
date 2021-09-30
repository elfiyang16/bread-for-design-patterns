class BreadOven {
  constructor() {
    this._startOven = true;
  }
  bake_bread(quantity, name) {
    this.quantity = quantity;
    this.name = name;
  }
  put_on_shelf() {
    return `${this.quantity} of ${this.name} are put on shelf!`;
  }
}

const BreadSingleton = (function () {
  let breadInstance;

  return {
    getInstance: function () {
      if (!breadInstance) {
        breadInstance = new BreadOven();
        delete breadInstance.constructor;
      }
      return breadInstance;
    },
  };
})();

let oven1 = BreadSingleton.getInstance();
oven1.bake_bread(5, "sourDough");
oven1.put_on_shelf();

let oven2 = BreadSingleton.getInstance();
oven2.bake_bread(10, "ciabatta");
oven2.put_on_shelf();

class BreadSingletonTwo {
  constructor() {
    if (!BreadSingletonTwo.instance) {
      this._oven = new BreadOven();
      BreadSingletonTwo.instance = this;
    }

    return BreadSingletonTwo.instance;
  }

  bake_bread(quantity, name) {
    return this._oven.bake_bread(quantity, name);
  }
  put_on_shelf() {
    return this._oven.put_on_shelf();
  }
}

const oven = new BreadSingletonTwo();
Object.freeze(oven);
// export default oven;

oven.bake_bread(10, "ciabatta");
oven.put_on_shelf();

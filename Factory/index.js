let breadFactoryWarehouse = {};

breadFactoryWarehouse["Ciabatta"] = class Ciabatta {
  constructor(quantity) {
    this.quantity = quantity;
  }
  makeBread() {
    return `Making ${this.quantity} of Ciabatta!`;
  }
};

breadFactoryWarehouse["Sourdough"] = class Sourdough {
  constructor(quantity) {
    this.quantity = quantity;
  }

  makeBread() {
    return `Making ${this.quantity} of Sourdough!`;
  }
};

class BreadFactory {
  constructor(type, quantity) {
    return new breadFactoryWarehouse[type](quantity);
  }
}

const sourdough = new BreadFactory("Sourdough", 5);
sourdough.makeBread;

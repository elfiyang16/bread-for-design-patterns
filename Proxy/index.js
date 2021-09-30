sleep = (m) => new Promise((r) => setTimeout(r, m));

class Bread {
  constructor() {}

  async labelBread(kind) {
    switch (kind) {
      case "Sourdough":
        await sleep(10);
        return "Your sourdough is here!";
      case "Ciabatta":
        await sleep(100);
        return "Your ciabatta is here!";
      case "Rye bread":
        await sleep(30);
        return "Your rye bread is here!";
    }
  }
}

class BreadProxy {
  constructor() {
    this.cache = {};
    this.bread = new Bread();
  }

  async labelBread(kind) {
    if (this.cache[kind] == null) {
      this.cache[kind] = await this.bread.labelBread(kind);
    }
    return this.cache[kind];
  }
}

const breadProxy = new BreadProxy();
(async () => {
  await breadProxy.labelBread("Sourdough");
  await breadProxy.labelBread("Sourdough");
  await breadProxy.labelBread("Ciabatta");
  await breadProxy.labelBread("Sourdough");
})();

class BreadFlyweightFactory {
  private flyweights: Record<string, BreadFlyweight> = {};

  constructor() {}

  public get_bread_flyweight(flour_kind, kind): BreadFlyweight {
    let bread;
    if (kind in this.flyweights) {
      bread = this.flyweights[kind];
    } else {
      this.flyweights[kind] = new BreadFlyweight(flour_kind, kind);
      bread = this.flyweights[kind];
    }

    return bread;
  }
}

class BreadFlyweight {
  public kind: string;
  public flour_kind: string;

  constructor(flour_kind, kind) {
    this.kind = kind;
    this.flour_kind = flour_kind;
  }

  public wait_for_bake(min) {
    return `${this.kind} is waiting for bake in ${min}!`;
  }
  public wait_for_fry(min) {
    return `${this.kind} is waiting for fry in ${min}!`;
  }
  public wait_for_toast(min) {
    return `${this.kind} is waiting for taost in ${min}!`;
  }
}

const bread_factory = new BreadFlyweightFactory();
const sourDough = bread_factory.get_bread_flyweight("wholemeal", "sourdough");
sourDough.wait_for_toast(30);

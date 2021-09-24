class BreadAdaptee {
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

  label_bread(kind) {
    this.kind = kind;
  }

  choose_flour(flour_kind) {
    this.flour_kind = flour_kind;
  }

  wait_for_bake(bake_in_min, temp) {
    this.bake_in_min = bake_in_min;
    this.temp = temp;
  }
}
class BreadAdapter {
  constructor() {
    this.bread = new BreadAdaptee();
  }
  operation(operation, ...args) {
    switch (operation) {
      case "labelBread":
        return this.bread.label_bread(args);
      case "chooseFlour":
        return this.bread.choose_flour(args);
      case "waitForBake":
        return this.bread.wait_for_bake(args);
      default:
        return undefined;
    }
  }
}

//Client call:

const breadAdapter = new BreadAdapter();
breadAdapter.operation("chooseFlour", "wholemeal");

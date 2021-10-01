// Option 1. pass in function as observer directly

class BreadObservable1 {
  observers = new Set();

  subscribe(func) {
    this.observers.add(func);
  }

  unsubscribe(func) {
    this.observers.delete(func);
  }

  notify(data) {
    this.observers.forEach((observer) => observer(data));
  }
}

const labelBread = (kind) => {
  console.log(`A bread marked as ${kind}`);
};
const bakeBread = (kind) => {
  console.log(`A bread baked as ${kind}`);
};
const waitForRise = (kind) => {
  console.log(`Waiting for ${kind} to rise`);
};

const breadObserver = new BreadObservable1();
breadObserver.subscribe(labelBread);
breadObserver.subscribe(bakeBread);
breadObserver.subscribe(waitForRise);
breadObserver.unsubscribe(waitForRise);

breadObserver.notify("Sourdough");

// Option 2. pass in class instances as observer which implement the `update` method in themselves

class BreadObservable2 {
  observers = new Set();

  subscribe(func) {
    this.observers.add(func);
  }

  unsubscribe(func) {
    this.observers.delete(func);
  }

  notify(data) {
    this.observers.forEach((observer) => observer.update(data));
  }
}

class LabelBreadObserver {
  update(kind) {
    console.log(`A bread marked as ${kind}`);
  }
}
class BakeBreadObserver {
  update(kind) {
    console.log(`A bread baked as ${kind}`);
  }
}
class WaitForRiseBreadObserver {
  update(kind) {
    console.log(`Waiting for ${kind} to rise`);
  }
}

const breadObserver2 = new BreadObservable2();
breadObserver2.subscribe(new LabelBreadObserver());
breadObserver2.subscribe(new BakeBreadObserver());
breadObserver2.subscribe(new WaitForRiseBreadObserver());
breadObserver2.unsubscribe(new WaitForRiseBreadObserver());

breadObserver2.notify("Sourdough");

//Option3. Adding state management

class BreadObservable3 {
  observers = new Set();
  state = {};

  subscribe(func) {
    this.observers.add(func);
  }

  unsubscribe(func) {
    this.observers.delete(func);
  }

  notify(data) {
    this.state = Object.assign(this.state, data);
    this.observers.forEach((observer) => observer.update(this.data));
  }

  get() {
    return this.state;
  }
}

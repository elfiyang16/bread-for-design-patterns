import asyncio
from abc import ABCMeta, abstractmethod


class IBread(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def label_bread():
        pass


class Bread(IBread):
    kind_match = {
        "Sourdough": "Your sourdough is here!",
        "Ciabatta": "Your ciabatta is here!",
        "Rye bread": "Your rye bread is here!",
    }

    def __init__(self):
        pass

    async def label_bread(self, kind):
        await asyncio.sleep(100)
        return self.kind_match.get(kind)


class BreadProxy(IBread):
    def __init__(self):
        self.cache = {}
        self.bread = Bread()

    async def label_bread(self, kind):
        if not self.cache.get(kind):
            self.cache[kind] = await self.bread.label_bread(kind)
            return self.cache[kind]
        return self.cache[kind]


async def main():
    breadProxy = BreadProxy()
    await breadProxy.label_bread("Sourdough")
    await breadProxy.label_bread("Sourdough")
    await breadProxy.label_bread("Ciabatta")
    await breadProxy.label_bread("Sourdough")

if __name__ == "__main__":
    asyncio.run(main())

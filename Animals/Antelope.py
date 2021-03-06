from random import randint

from Animal import Animal


class Antelope(Animal):
    def __init__(self, positionX, positionY, world):
        super().__init__(positionX, positionY, world)
        self.strength = 4
        self.initiative = 4
        self.step = 2

    def collision(self, org):
        if randint(0, 100) <= 50:
            self.movementOnFree()
            return False
        else:
            return super().collision(org)

    def spawn(self, x, y, world):
        self.world.addOrganism(Antelope(x, y, world))


import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


def rollDice(sides=6):
    return random.randint(1, sides)


d = Dice(90)
# print(d.roll())
print(rollDice())

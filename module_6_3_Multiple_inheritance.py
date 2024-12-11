import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _cords=[0,0,0]):
        self.speed = speed
        self.cords = _cords

    def move(self, dx, dy, dz):
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self.cords[0] = dx * self.speed
            self.cords[1] = dy * self.speed
            self.cords[2] = dz * self.speed

    def get_cords(self):
        print(f"X: {self.cords[0]} Y: {self.cords[1]} Z: {self.cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        rnd_num = random.randrange(1, 5)
        print(f"Here are(is) {rnd_num} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        self.cords[2] -= int(abs(-dz) * (self.speed / 2))


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


print(Duckbill.mro())

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()
print(db._DEGREE_OF_DANGER)

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

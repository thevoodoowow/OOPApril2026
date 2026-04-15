class Bird:
    def alive(self) -> str:
        return "Птица живет"


class FlyingBird(Bird):
    def fly(self) -> str:
        return "Лечу!"


class Sparrow(FlyingBird):
    def fly(self) -> str:
        return "Воробей летит"


class Penguin(Bird):
    def step(self) -> str:
        return "Пингвин ходит"


def make_birds_fly(birds: list[FlyingBird]):
    for bird in birds:
        print(bird.fly())


birds = [Sparrow()]
make_birds_fly(birds)

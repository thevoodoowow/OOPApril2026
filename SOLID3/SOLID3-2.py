from abc import abstractmethod


class Figure:
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Figure):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side**2


def print_area(figure: Figure):
    print(f"Площадь: {figure.area()}")


print_area(Rectangle(2, 3))
print_area(Square(2))

class AreaCalculator:
    def calculate(self, shape: dict) -> float:
        if shape['type'] == 'circle':
            return 3.14159 * shape['radius'] ** 2
        elif shape['type'] == 'rectangle':
            return shape['width'] * shape['height']

class AreaCalculator1(AreaCalculator):
    def calculate(self, shape: dict) -> float:
        if shape['type'] == 'triangle':
            return 0.5 * shape['base'] * shape['height']
        return super().calculate(shape)

calc = AreaCalculator1()


print(calc.calculate({'type': 'circle', 'radius': 5})) 
print(calc.calculate({'type': 'rectangle', 'width': 4, 'height': 6}))
print(calc.calculate({'type': 'triangle', 'base': 10, 'height': 5}))

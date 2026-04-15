class Pizza:
    def __init__(self):
        self.size: str = ""
        self.dough: str = ""
        self.sauce: str = ""
        self.cheese: str = ""
        self.toppings: list[str] = []

    def __str__(self) -> str:
        toppings = ", ".join(self.toppings) if self.toppings else "без топпингов"
        return (
            f"Пицца {self.size} на {self.dough} тесте\n"
            f"Соус: {self.sauce}, Сыр: {self.cheese}\n"
            f"Топпинги: {toppings}\n"
        )


# Строитель


class PizzaBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._pizza = Pizza()
        return self

    def set_size(self, size: str):
        self._pizza.size = size
        return self

    def set_dough(self, dough: str):
        self._pizza.dough = dough
        return self

    def set_sauce(self, sauce: str):
        self._pizza.sauce = sauce
        return self

    def set_cheese(self, cheese: str):
        self._pizza.cheese = cheese
        return self

    def add_topping(self, topping: str):
        self._pizza.toppings.append(topping)
        return self

    def build(self) -> Pizza:
        if not self._pizza.size or not self._pizza.dough:
            raise ValueError("Ошибка: Размер и тип теста должны быть указаны!")

        product = self._pizza
        self.reset()
        return product


# Директор


class Director:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def build_margherita(self) -> Pizza:
        return (
            self.builder.set_size("M")
            .set_dough("традиционное")
            .set_sauce("томатный")
            .set_cheese("моцарелла")
            .add_topping("базилик")
            .build()
        )

    def build_pepperoni(self) -> Pizza:
        return (
            self.builder.set_size("L")
            .set_dough("тонкое")
            .set_sauce("томатный")
            .set_cheese("моцарелла")
            .add_topping("пепперони")
            .build()
        )

    def build_vegetarian(self) -> Pizza:
        return (
            self.builder.set_size("M")
            .set_dough("тонкое")
            .set_sauce("томатный")
            .set_cheese("сыр для соевых")
            .add_topping("томаты")
            .add_topping("перец")
            .add_topping("оливки")
            .build()
        )


# Клиентский код

builder = PizzaBuilder()
director = Director(builder)

# Заказ через директора
print("Маргарита")
print(director.build_margherita())

print("Пепперони")
print(director.build_pepperoni())

print("Соевая пицца")
print(director.build_vegetarian())

# Произвольная пицца
print("Произвольная пицца")
custom_pizza = (
    builder.set_size("XL")
    .set_dough("пышное")
    .set_sauce("барбекю")
    .add_topping("бекон")
    .add_topping("ананасы")
    .build()
)
print(custom_pizza)

# Ошибка (не указано размер и тесто)
try:
    bad_pizza = PizzaBuilder().set_size("S").build()
except ValueError as e:
    print(f"Ошибка: {e}")

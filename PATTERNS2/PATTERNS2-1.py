from abc import abstractmethod


class Button:
    @abstractmethod
    def render(self) -> str:
        pass


class Checkbox:
    @abstractmethod
    def render(self) -> str:
        pass


class Input:
    @abstractmethod
    def render(self) -> str:
        pass


class LightButton(Button):
    def render(self) -> str:
        return "[Light Button]"


class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "[Light Checkbox]"


class LightInput(Input):
    def render(self) -> str:
        return "[Light Input]"


class DarkButton(Button):
    def render(self) -> str:
        return "[Dark Button]"


class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "[Dark Checkbox]"


class DarkInput(Input):
    def render(self) -> str:
        return "[Dark Input]"


class UIFactory:
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

    @abstractmethod
    def create_input(self) -> Input:
        pass


class LightThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()

    def create_input(self) -> Input:
        return LightInput()


class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()

    def create_input(self) -> Input:
        return DarkInput()


class Application:
    def __init__(self, factory: UIFactory):

        self.factory = factory

    def render_ui(self):
        btn = self.factory.create_button()
        chk = self.factory.create_checkbox()
        inp = self.factory.create_input()
        print(btn.render(), chk.render(), inp.render())


factory = DarkThemeFactory()
app = Application(factory)
app.render_ui()

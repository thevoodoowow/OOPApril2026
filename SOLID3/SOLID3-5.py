class Read:
    def read(self, key: str) -> str:
        return f"Данные по ключу {key}"


class Write(Read):
    def write(self, key: str, value: str):
        print(f"Запись: {key} = {value}")


class ReadOnlyStorage(Read):
    pass


class Storage(Write):
    pass


def save_data(storage: Write, key: str, value: str):
    storage.write(key, value)
    print(storage.read(key))


# Вызовы
save_data(Storage(), "user", "Алексей")

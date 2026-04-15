from abc import abstractmethod


class Reader:
    @abstractmethod
    def find(self, id: int):
        pass


class Writer:
    @abstractmethod
    def save(self, entity: dict):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass


class Exporter:
    @abstractmethod
    def export_csv(self) -> str:
        pass


class ReadOnlyRepository(Reader):
    def find(self, id: int):
        return {"id": id, "name": "Иван"}


class UserRepository(Reader, Writer, Exporter):
    def find(self, id: int):
        return {"id": id, "name": "Анна"}

    def save(self, entity: dict):
        print(f"Сохранение: {entity}")

    def delete(self, id: int):
        print(f"Удаление id={id}")

    def export_csv(self) -> str:
        return "id,name\n1,Анна"


def update_user(repo: Writer, user_data: dict):
    repo.save(user_data)


def display_user(repo: Reader, user_id: int):
    print(repo.find(user_id))


read_only = ReadOnlyRepository()
full_repo = UserRepository()

display_user(read_only, 1)
display_user(full_repo, 2)
update_user(full_repo, {"name": "Новый"})

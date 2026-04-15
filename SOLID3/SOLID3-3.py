class FileReader:
    def read(self, path: str) -> str:
        return f"Содержимое файла: {path}"


class NetworkFileReader(FileReader):
    def __init__(self, available: bool):
        self.available = available

    def read(self, path: str) -> str:
        if not self.available:
            raise ConnectionError("Сеть недоступна")
        return f"Содержимое по сети: {path}"


def process(reader: FileReader, path: str):
    try:
        content = reader.read(path)
        print(content.upper())
    except (FileNotFoundError, ConnectionError) as e:
        print(f"Ошибка чтения: {e}")


process(FileReader(), "local.txt")
process(NetworkFileReader(available=False), "remote.txt")

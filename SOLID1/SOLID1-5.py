import csv, io


class CsvParser:
    @staticmethod
    def parse(csv_content: str) -> list[dict]:
        reader = csv.DictReader(io.StringIO(csv_content))
        return [row for row in reader]


class FileStorage:
    @staticmethod
    def save_to_csv(data: list[dict], outputpath: str):
        if not data:
            return
        with open(outputpath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


content = "name,age\nАнна,30\nИван,25"

data = CsvParser.parse(content)

FileStorage.save_to_csv(data, "output.csv")

for row in data:
    print(row)

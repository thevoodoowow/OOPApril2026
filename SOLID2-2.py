import json, csv, io

# Нарушение OCP
class DataExporter:
    def export(self, data: list[dict], format: str) -> str:
        if format == 'json':
            return json.dumps(data, ensure_ascii=False)
        elif format == 'csv':
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            return output.getvalue()
        
import xml.etree.ElementTree as ET

class DataExporter1(DataExporter):
    def export(self, data: list[dict], format: str) -> str:
        if format == 'xml':
            root = ET.Element("root")
            for item in data:
                entry = ET.SubElement(root, "entry")
                for key, val in item.items():
                    child = ET.SubElement(entry, key)
                    child.text = str(val)
            return ET.tostring(root, encoding='unicode')
        
        return super().export(data, format)

# Вызов
exporter = DataExporter1()
records = [{'name': 'Анна', 'age': 30}, {'name': 'Иван', 'age': 25}]
print(exporter.export(records, 'xml'))
print(exporter.export(records, 'json'))
print(exporter.export(records, 'csv'))

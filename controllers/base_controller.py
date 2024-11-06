import csv
from typing import List, Type, TypeVar

T = TypeVar('T')

class CSVController:
    def __init__(self, file_path: str, model: Type[T]):
        self.file_path = file_path
        self.model = model

    def get_all(self) -> List[T]:
        instances = []
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    # Map CSV row data to model attributes
                    instance = self.model(**row)
                    instances.append(instance)
            return instances
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []
        except TypeError as e:
            print(f"Error creating instance of {self.model.__name__}: {e}")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
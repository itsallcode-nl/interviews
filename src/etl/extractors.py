import json

from etl.dataset import DataSet


class FileExtractor:
    @staticmethod
    def extract(file_path: str) -> DataSet:
        with open(file_path, 'r') as f:
            data: list[dict] = json.load(f)
            return DataSet(data)
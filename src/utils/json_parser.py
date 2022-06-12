import json
import os


class JsonParser:
    def __init__(self, file_name, relative_path):
        __root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        self.file_name = file_name
        self.relative_path = relative_path
        self.file_path = os.path.join(__root_path, self.relative_path, self.file_name)

    def read_from_json(self):
        with open(self.file_path, 'r') as json_file:
            return json.load(json_file)

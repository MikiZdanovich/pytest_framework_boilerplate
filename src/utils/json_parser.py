import json
import os


class JsonParser:
    def __init__(self, file_name, path):
        self.file_name = file_name
        self.path = path
        self.file_path = os.path.join(self.path, self.file_name)

    def read_from_json(self):
        with open(self.file_path, 'r') as json_file:
            return json.load(json_file)

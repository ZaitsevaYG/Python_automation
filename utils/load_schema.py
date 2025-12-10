import json
import os


def load_schema(filename: str):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schema_path = os.path.join(project_root, 'schema', filename)


    with open(schema_path, encoding='utf-8') as file:  # Указываем кодировку
        schema = json.load(file)
        return schema
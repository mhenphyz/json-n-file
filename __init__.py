import json
from pathlib import Path
from .jsonFileExceptions import FilePathNotDefined


class JSN():

    file = None
    file_path = None
    file_content = None
    json_content = None

    @classmethod
    def __check_file(cls):
        if cls.file_path is None:
            raise FilePathNotDefined

    @classmethod
    def __read_file(cls):
        cls.__check_file()
        cls.file = open(cls.file_path, 'r')
        cls.file_content = cls.file

    @classmethod
    def __write_file(cls, data):
        cls.__check_file()
        cls.file = open(cls.file_path, 'w')
        json.dump(data, cls.file, sort_keys=True)
        cls.__close_file()

    @classmethod
    def __close_file(cls):
        cls.file.close()

    @classmethod
    def __json_load(cls):
        cls.json_content = json.load(cls.file_content)

    @classmethod
    def set_file(cls, file_path):
        cls.file_path = Path(file_path)

    @classmethod
    def read(cls):
        cls.__read_file()
        cls.__json_load()
        cls.__close_file()
        return cls.json_content

    @classmethod
    def write(cls, data: dict):
        cls.__write_file(data)
        return True

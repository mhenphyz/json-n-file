# -*- coding:utf-8 -*-


class FilePathNotDefined(Exception):
    def __init__(self):
        Exception.__init__(self, "file_path attribute is not defined")

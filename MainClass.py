from project.MainClass import MainClass

import os

def deco(color: str):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "reset": "\033[0m"
    }
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(colors.get(color, ""), end="")
            result = func(*args, **kwargs)
            print(colors["reset"], end="")
            return result
        return wrapper
    return decorator

class MainClass:
    """
    A class to read and concatenate text files with extra capabilities.
    """

    def __init__(self, filepath):
        # Constructor checks if given file is a .txt and exists
        if not filepath.endswith('.txt'):
            raise ValueError("Only .txt files are supported.")
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        self._filepath = filepath

    @property
    def filepath(self):
        # Getter for filepath
        return self._filepath

    @filepath.setter
    def filepath(self, new_path):
        # Setter with validation
        if not new_path.endswith('.txt'):
            raise ValueError("Only .txt files are supported.")
        self._filepath = new_path

    def read_lines(self):
        """
        Generator to read lines one by one from file.
        """
        with open(self._filepath, 'r') as f:
            for line in f:
                yield line.strip()

    def read_words_as_list(self):
        """
        Returns all words in the file using list comprehension.
        """
        with open(self._filepath, 'r') as f:
            return [word for line in f for word in line.strip().split()]

    def __str__(self):
        return f"MainClass for {self._filepath}"

    def __add__(self, other):
        """
        Overloads + operator to combine two files.
        """
        return self.concat_files(self._filepath, other._filepath)

    @staticmethod
    def file_exists(path):
        """
        Check if a file exists at path.
        """
        return os.path.exists(path)

    @classmethod
    def from_path(cls, path):
        """
        Alternative constructor using a file path.
        """
        return cls(path)

    @staticmethod
    @deco("green")
    def concat_files(path1, path2):
        """
        Concatenates two files into one.
        """
        output = "combined.txt"
        with open(output, 'w') as out:
            for path in [path1, path2]:
                with open(path, 'r') as f:
                    out.write(f.read())
        return MainClass(output)

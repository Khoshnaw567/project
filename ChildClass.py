
from MainClass import MainClass, deco

class ChildClass(MainClass):
    """
    Inherits MainClass and adds ability to concatenate many files.
    """

    def __str__(self):
        return f"ChildClass for {self.filepath}"

    @deco("yellow")
    def concat_many_files(self, *paths):
        """
        Concatenate contents of multiple files into a new file.
        """
        output = "files_combined.txt"
        with open(output, 'w') as out:
            for path in paths:
                with open(path, 'r') as f:
                    out.write(f.read())
        return MainClass(output)

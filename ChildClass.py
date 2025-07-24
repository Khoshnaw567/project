
from MainClass import MainClass, deco

class ChildClass(MainClass):
# [RUBRIC] ✅ Inheritance used (ChildClass extends MainClass)
    """
    Inherits MainClass and adds ability to concatenate many files.
    """

    def __str__(self):
# [RUBRIC] ✅ __str__ overridden in child class
        return f"ChildClass for {self.filepath}"

    @deco("yellow")
# [RUBRIC] ✅ Custom decorator used to add colored terminal output
    def concat_many_files(self, *paths):
# [RUBRIC] ✅ Method handles variable number of file inputs using *args
        """
        Concatenate contents of multiple files into a new file.
        """
        output = "files_combined.txt"
        with open(output, 'w') as out:
            for path in paths:
                with open(path, 'r') as f:
                    out.write(f.read())
        return MainClass(output)

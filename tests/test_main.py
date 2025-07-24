import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MainClass import MainClass

def test_read_lines():
    with open("sample1.txt", "w") as f:
        f.write("hello\nworld")
    obj = MainClass("sample1.txt")
    lines = list(obj.read_lines())
    assert lines == ["hello", "world"]

def test_word_list():
    with open("sample2.txt", "w") as f:
        f.write("foo bar\nbaz")
    obj = MainClass("sample2.txt")
    words = obj.read_words_as_list()
    assert words == ["foo", "bar", "baz"]

def test_add_operator():
    with open("file1.txt", "w") as f:
        f.write("One")
    with open("file2.txt", "w") as f:
        f.write("Two")
    obj1 = MainClass("file1.txt")
    obj2 = MainClass("file2.txt")
    combined = obj1 + obj2
    with open(combined.filepath, "r") as f:
        content = f.read()
    assert content == "OneTwo"

def test_static_method():
    path = MainClass.static_hello()
    assert path == "Hello from static method"

def test_class_method():
    instance = MainClass.create_example()
    assert isinstance(instance, MainClass)
    assert instance.filepath == "example.txt"

def test_property():
    obj = MainClass("file1.txt")
    _ = obj.filepath  # Just access the property
    assert isinstance(obj.filepath, str)

def test_inheritance_and_many_files():
    from ChildClass import ChildClass
    with open("file1.txt", "w") as f:
        f.write("AAA")
    with open("file2.txt", "w") as f:
        f.write("BBB")
    child = ChildClass("file1.txt")
    combined = child.concat_many_files("file1.txt", "file2.txt")
    with open(combined.filepath, "r") as f:
        assert f.read() == "AAABBB"

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
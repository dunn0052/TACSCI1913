import inspect
import re
import importlib.util

#test file
def test(file, name, path = None):
    spec = importlib.util.spec_from_file_location(file, path)
    test = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test)
    #lookFor(file, "list")
    #test = __import__(file)
    data = []
    data.append(name)
    return data


def testItem(function, key):
    try:
        return function == key
    except:
        print("Couldn't run", str(function), "for", name)

def lookFor(file, pattern, src):
    src.getsource(__import__(file))
    capture = re.compile(pattern)
    s = capture.findall(src)
    if s:
        print(s)

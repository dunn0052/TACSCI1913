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
    data.append(test.isInside('x', 'x') == True)
    data.append(test.isInside('x', 'y') ==  False)
    data.append(test.isInside('x', ('x', '+', 'y')) ==  True)
    data.append(test.isInside('x', ('a', '+', 'b')) ==  False)
    data.append(test.isInside('+', ('a', '+', 'b')) ==  False)
    data.append(test.isInside('x', (('m', '*', 'x'), '+', 'b')) == True)

    data.append(test.solve('x', (('a', '+', 'x'), '=', 'c')) ==  ('x', '=', ('c', '-', 'a')))

    data.append(test.solve('x', (('x', '+', 'b'), '=', 'c')) ==  ('x', '=', ('c', '-', 'b')))

    data.append(test.solve('x', (('a', '-', 'x'), '=', 'c')) ==  ('x', '=', ('a', '-', 'c')))

    data.append(test.solve('x', (('x', '-', 'b'), '=', 'c')) ==  ('x', '=', ('c', '+', 'b')))

    data.append(test.solve('x', (('a', '*', 'x'), '=', 'c')) ==  ('x', '=', ('c', '/', 'a')))

    data.append(test.solve('x', (('x', '*', 'b'), '=', 'c')) ==  ('x', '=', ('c', '/', 'b')))

    data.append(test.solve('x', (('a', '/', 'x'), '=', 'c')) ==  ('x', '=', ('a', '/', 'c')))

    data.append(test.solve('x', (('x', '/', 'b'), '=', 'c')) ==  ('x', '=', ('c', '*', 'b')))

    data.append(test.solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))) == ('y', '=', (('m', '*', 'x'), '+', 'b')))

    data.append(test.solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))) == ('x', '=', (('y', '-', 'b'), '/', 'm')))

    data.append(test.solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))) == ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e')))
    return data


def testItem(function, key):
    return function == key

def lookFor(file, pattern):
    src = inspect.getsource(__import__(file))
    capture = re.compile(pattern)
    s = capture.findall(src)
    if s:
        print(s)


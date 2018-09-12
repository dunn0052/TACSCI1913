==test file
def test(file, name):
    test = __import__(file)
    data = []
    data.append(name)
    test.isInside('x', 'x')) == True
    test.isInside('x', 'y')) ==  False
    test.isInside('x', ('x', '+', 'y'))) ==  True
    test.isInside('x', ('a', '+', 'b'))) ==  False
    test.isInside('+', ('a', '+', 'b'))) ==  False
    test.isInside('x', (('m', '*', 'x'), '+', 'b'))) == True

    test.solve('x', (('a', '+', 'x'), '=', 'c'))) ==  ('x', '=', ('c', '-', 'a'))

    test.solve('x', (('x', '+', 'b'), '=', 'c'))) ==  ('x', '=', ('c', '-', 'b'))

    test.solve('x', (('a', '-', 'x'), '=', 'c'))) ==  ('x', '=', ('a', '-', 'c'))

    test.solve('x', (('x', '-', 'b'), '=', 'c'))) ==  ('x', '=', ('c', '+', 'b'))

    test.solve('x', (('a', '*', 'x'), '=', 'c'))) ==  ('x', '=', ('c', '/', 'a'))

    test.solve('x', (('x', '*', 'b'), '=', 'c'))) ==  ('x', '=', ('c', '/', 'b'))

    test.solve('x', (('a', '/', 'x'), '=', 'c'))) ==  ('x', '=', ('a', '/', 'c'))

    test.solve('x', (('x', '/', 'b'), '=', 'c'))) ==  ('x', '=', ('c', '*', 'b'))

    test.solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b')))) == ('y', '=', (('m', '*', 'x'), '+', 'b'))

    test.solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b')))) == ('x', '=', (('y', '-', 'b'), '/', 'm'))

    test.solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f'))))) == ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))

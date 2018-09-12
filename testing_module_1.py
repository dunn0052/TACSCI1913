#test file
def test(file, name):
    test = __import__(file)
    data = []
    data.append(name)
    data.append(test.isInside(('x', 'x')) == True)
    data.append(test.isInside(('x', 'y')) ==  False)
    data.append(test.isInside(('x', ('x', '+', 'y'))) ==  True)
    data.append(test.isInside(('x', ('a', '+', 'b'))) ==  False)
    data.append(test.isInside(('+', ('a', '+', 'b'))) ==  False)
    data.append(test.isInside(('x', (('m', '*', 'x'), '+', 'b'))) == True)

    data.append(test.solve(('x', (('a', '+', 'x'), '=', 'c'))) ==  ('x', '=', ('c', '-', 'a')))

    data.append(test.solve(('x', (('x', '+', 'b'), '=', 'c'))) ==  ('x', '=', ('c', '-', 'b')))

    data.append(test.solve(('x', (('a', '-', 'x'), '=', 'c'))) ==  ('x', '=', ('a', '-', 'c')))

    data.append(test.solve(('x', (('x', '-', 'b'), '=', 'c'))) ==  ('x', '=', ('c', '+', 'b')))

    data.append(test.solve(('x', (('a', '*', 'x'), '=', 'c'))) ==  ('x', '=', ('c', '/', 'a')))

    data.append(test.solve(('x', (('x', '*', 'b'), '=', 'c'))) ==  ('x', '=', ('c', '/', 'b')))

    data.append(test.solve(('x', (('a', '/', 'x'), '=', 'c'))) ==  ('x', '=', ('a', '/', 'c')))

    data.append(test.solve(('x', (('x', '/', 'b'), '=', 'c'))) ==  ('x', '=', ('c', '*', 'b')))

    data.append(test.solve(('y', ('y', '=', (('m', '*', 'x'), '+', 'b')))) == ('y', '=', (('m', '*', 'x'), '+', 'b')))

    data.append(test.solve(('x', ('y', '=', (('m', '*', 'x'), '+', 'b')))) == ('x', '=', (('y', '-', 'b'), '/', 'm')))

    data.append(test.solve(('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f'))))) == ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e')))

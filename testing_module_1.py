#test file
def test(file, name):
    test = __import__(file) 
    data = []
    data.append(name)
    print(test.isInside('x', 'x'))                          #  True   1 point
    print(test.isInside('x', 'y'))                          #  False  1 point
    print(test.isInside('x', ('x', '+', 'y')))              #  True   2 points
    print(test.isInside('x', ('a', '+', 'b')))              #  False  2 points
    print(test.isInside('+', ('a', '+', 'b')))              #  False  2 points
    print(test.isInside('x', (('m', '*', 'x'), '+', 'b')))  #  True   2 points

    print(test.solve('x', (('a', '+', 'x'), '=', 'c')))
    #  ('x', '=', ('c', '-', 'a'))  2 points

    print(test.solve('x', (('x', '+', 'b'), '=', 'c')))
    #  ('x', '=', ('c', '-', 'b'))  2 points

    print(test.solve('x', (('a', '-', 'x'), '=', 'c')))
    #  ('x', '=', ('a', '-', 'c'))  2 points

    print(test.solve('x', (('x', '-', 'b'), '=', 'c')))
    #  ('x', '=', ('c', '+', 'b'))  2 points

    print(test.solve('x', (('a', '*', 'x'), '=', 'c')))
    #  ('x', '=', ('c', '/', 'a'))  2 points

    print(test.solve('x', (('x', '*', 'b'), '=', 'c')))
    #  ('x', '=', ('c', '/', 'b'))  2 points

    print(test.solve('x', (('a', '/', 'x'), '=', 'c')))
    #  ('x', '=', ('a', '/', 'c'))  2 points

    print(test.solve('x', (('x', '/', 'b'), '=', 'c')))
    #  ('x', '=', ('c', '*', 'b'))  2 points

    print(test.solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
    # ('y', '=', (('m', '*', 'x'), '+', 'b'))  2 points

    print(test.solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
    # ('x', '=', (('y', '-', 'b'), '/', 'm'))  2 points

    print(test.solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))
    # ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))  5 points

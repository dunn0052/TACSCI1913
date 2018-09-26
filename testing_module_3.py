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
## begin testing code here

    data.append(testItem(test.Maximum((1,)), 1))                      #  1                            2 pt.
    data.append(testItem(test.Maximum((1, 2)), 2))                    #  2                            2 pt.
    data.append(testItem(test.Maximum((1, 1)), 1))                    #  1                            2 pt.
    data.append(testItem(test.Maximum((1, 2, 3)), 3))                 #  3                            2 pt.

    data.append(testItem(test.Remove((), 1), ()))                      #  ()                           2 pt.
    data.append(testItem(test.Remove((1,), 1), ()))                    #  ()                           2 pt.
    data.append(testItem(test.Remove((0, 1), 0), (1,)))                  #  (1,)                         2 pt.
    data.append(testItem(test.Remove((0, 1, 2, 1, 3), 1), (0,2,1,3)))         #  (0, 2, 1, 3)                 2 pt.
    data.append(testItem(test.Remove((0, 1, 2, 1, 3), 2), (0,1,1,3)) )        #  (0, 1, 1, 3)                 2 pt.
    data.append(testItem(test.Remove((1, 2, 3), 3), (1,2))            )   #  (1, 2)                       2 pt.

    data.append(testItem(test.Sort(()), ())                           )#  ()                           2 pt.
    data.append(testItem(test.Sort((0,)), (0,))                        ) #  (0,)                         2 pt.
    data.append(testItem(test.Sort((0, 1)),(0,1))                       )#  (0, 1)                       2 pt.
    data.append(testItem(test.Sort((1, 0)),(0,1))                       )#  (0, 1)                       2 pt.
    data.append(testItem(test.Sort((0, 0, 1)),(0,0,1))                   ) #  (0, 0, 1)                    2 pt.
    data.append(testItem(test.Sort((0, 1, 0)), (0,0,1))                   ) #  (0, 0, 1)                    2 pt.
    data.append(testItem(test.Sort((0, 0, 1)), (0,0,1))                    )#  (0, 0, 1)                    2 pt.

    data.append(testItem(test.Sort((9, 8, 7, 6, 5, 4, 3, 2, 1)), (1,2,3,4,5,6,7,8,9)) ) #  (1, 2, 3, 4, 5, 6, 7, 8, 9)  2 pt.
    data.append(testItem(test.Sort((1, 2, 3, 4, 5, 6, 7, 8, 9)), (1,2,3,4,5,6,7,8,9))  )#  (1, 2, 3, 4, 5, 6, 7, 8, 9)  2 pt.
    data.append(testItem(test.Sort((1, 2, 1, 4, 2, 5, 4, 5, 3)),(1,1,2,2,3,4,4,5,5))  )#  (1, 1, 2, 2, 3, 4, 4, 5, 5)  2 pt.
## end testing code here
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

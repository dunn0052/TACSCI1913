import javaRunner



def test(file, name, path = None):
    data = []
    test = ['00', '01', '02', '10', '11', '0000', '0999', '1000', '1999', '2000', '9999', '0000', '0001']

    #compile code
    javaRunner.javaC(path, file)

    # get code output
    output = javaRunner.javaR("Driver")
    check = zip(output, test)
    for c in check:
        data.append(c[0] == c[1])
    javaRunner.clear() #checkout to see that it works, but probably just compiles over it
    print(data)
    return data

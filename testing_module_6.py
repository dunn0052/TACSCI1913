import javaRunner, platform



def test(file, name, path = None):
    data = []

    #compile code
    javaRunner.javaC(path, file)

    # get code output
    output = javaRunner.javaR(path, "BinaryVsLinear")
    for p in output:
        print(p)
    javaRunner.clear(path)
    return data

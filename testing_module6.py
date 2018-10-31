import javaRunner, platform



def test(file, name, path = None):
    data = []

    #compile code
    javaRunner.javaC(path, file)

    # get code output
    output = javaRunner.javaR(path, "Driver")
    print(output)
    javaRunner.clear(path)
    return data

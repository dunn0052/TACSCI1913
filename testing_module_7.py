import javaRunner as J



def test(file, name, path = None):
    data = []
    test = ['true', '0', '0', 'No pop', 'No peek', 'A', '1', '1', 'false', 'B', '2', '2', 'B', '3', '2', 'B', '4', '2', 'C', '5', '3', 'C', '6', '3', 'C', '5', '3', 'B', '4', '2', 'B', '3', '2', 'A', '1', '1', 'true', '0', '0', 'No peek']
    #compile code
    J.javaC(path, file)

    # get code output
    output = J.javaR(path, "Camembert")
    check = zip(output, test)
    for c in check:
        data.append(c[0] == c[1])
    J.clear(path) #checkout to see that it works, but probably just compiles over it 
    return data

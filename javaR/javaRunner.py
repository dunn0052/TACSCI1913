import subprocess

def javaC(file):
    try:
        file = file + ".java"
        subprocess.run(["javac", file])
        print("Java compiled", file)
        return 0
    except:
        print("Couldn't compile", file)
        return -1

def javaR(file):
    out = subprocess.check_output(["java",file])
    out = out.decode("utf-8")
    list_out = out.split("\n")
    list_out.pop()
    print(list_out)

def clear():
    subrocess.run(["rm", "-f", "*.class"])
    

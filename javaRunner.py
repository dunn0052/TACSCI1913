import subprocess, platform

def javaC(file):
    try:
        command = ["javac", file+".java"]
        subprocess.run(command, shell=True)
        print("Java compiled", file+".java")
        return 0
    except:
        print("Couldn't compile", file)
        return -1

def javaR(path, file):
    out = subprocess.run(["java", "-cp", path, file], shell=True, capture_output=True).stdout
    out = out.decode("utf-8")
    list_out = out.split("\r\n")
    if list_out[-1] == "":
        list_out.pop()
    return list_out

def clear(path = None):
    sys = platform.system() #different commands for each system
    if sys == "Linux":
        subprocess.run(["rm", "-rf", path + "*.class"], shell=True)
    elif sys == "Windows":
        subprocess.run(["del", path + "*.class"], shell=True)

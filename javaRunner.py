import subprocess

def javaC(file):
    try:
        subprocess.run(["javac", file+".java"])
        print("Java compiled", file)
        return 0
    except:
        print("Couldn't compile", file)
        return -1

def javaR(file):
    out = subprocess.check_output(["java",file])
    out = out.decode("utf-8")
    list_out = out.split("\n")
    if list_out[-1] == "":
        list_out.pop()
    #print(list_out)
    return list_out

def clear():
    subprocess.run(["rm", "-f", "*.class"])
    

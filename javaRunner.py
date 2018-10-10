import subprocess, platform

def plat():
	return platform.system()

def javaC(path, file):
    try:
        command = ["javac", path+file+".java"]
        subprocess.run(command, shell=True)
        print("Java compiled", file+".java")
        return 0
    except:
        print("Couldn't compile", file)
        return -1

def javaR(path, file):
	if plat() == "Windows":
                out = subprocess.run(["java", "-cp", path, file], shell=True, capture_output=True).stdout
                out = out.decode("utf-8")
                list_out = out.split("\r\n")
	elif plat() == "Linux":
                out = subprocess.check_output(["java", "-classpath", path , file])
                out = out.decode("utf-8")
                list_out = out.split("\n")
	if list_out[-1] == "":
		list_out.pop()
	return list_out

def clear(path = None):
    sys = plat() #different commands for each system
 
    if sys == "Linux":
        print(path + "/*.class")
        subprocess.run(["rm", "-rf", path + "/*.class"], shell=True)
    elif sys == "Windows":
        subprocess.run(["del", path + "*.class"], shell=True)

import subprocess, platform, os

def plat():
        return platform.system()

def javaC(file):
        try:
                # must be path/file instead of /path/file
                command = ["javac", file+".java"]
                if plat() == "Windows":
                    subprocess.run(command, shell=True)
                elif plat() == "Linux":
                        subprocess.call(command)
                print("Java compiled", file+".java")
                return 0
        except:
                print("Couldn't compile", file)
                return -1

def javaR(path, file):
        #path = path no beginning or end backslash -- could remove via re
        #file = filename without .java
        if plat() == "Windows":
               out = subprocess.run(["java", "-cp", path, file], shell=True, capture_output=True).stdout
               out = out.decode("utf-8")
               list_out = out.split("\r\n")
        if plat() == "Linux":
                out = subprocess.check_output(["java", "-classpath", path, file])
                out = out.decode("utf-8")
                list_out = out.split("\n")
        if list_out[-1] == "":
                list_out.pop()
        return list_out

def clear(path = None):
        sys = plat() #different commands for each system
        if sys == "Linux":
                # remove individual files, path = "lab4_to_grade/Driver.class"
                os.remove(path)
        elif sys == "Windows":
                command = ["del", path + "*.class"]
                subprocess.run(command, shell=True)

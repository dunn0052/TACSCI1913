#grading script lab7

#set grading paths
lab_number = "7"
grade_path = "lab"+lab_number+"_to_grade"
score_path = "lab"+lab_number+"_scores"

import re
import os
import crw
import testing_module_7 as t
import platform
directory_path = os.path.dirname(os.path.realpath(__file__))

if platform.system() == "Windows":
    print("\\"+directory_path + "\\" + grade_path+"\\")
    labs = os.listdir(directory_path + "\\" + grade_path+"\\") #add \\ because java compiler doesn't takes path instead of /path
elif platform.system() == "Linux":
    labs= os.listdir("/"+directory_path+"/"+grade_path+"/") # if linux
    
data = []
reject = []
capture_string ="((.*)_lab"+lab_number+").java"

for lab in labs:
    capture = re.compile(capture_string)
    s = capture.findall(lab)
    if s != []:
        score = [s[0][1]]
        score += t.test(file = s[0][0], name = s[0][1], path = grade_path)
        data.append(score)
        print("Graded:", s[0][0], "\n")
    else:
        reject.append(lab)
        
if data:
    crw.setData(path = directory_path + "\\"+score_path+"\\" , title = "lab"+lab_number+"_scores", data = data)
    if reject:
        print("Files not graded", reject)
else:
    print("No labs were graded.")

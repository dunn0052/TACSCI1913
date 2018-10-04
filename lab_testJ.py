#grading script lab3

#set grading paths
lab_number = "4"
grade_path = "lab"+lab_number+"_to_grade\\"
score_path = "\\lab"+lab_number+"_scores\\"

import re
import os
import crw
import testing_module_4
directory_path = os.path.dirname(os.path.realpath(__file__))

labs = os.listdir(directory_path + "\\" + grade_path) #add // because java compiler doesn't takes path instead of /path
data = []
reject = []
capture_string ="((.*)_lab"+lab_number+").java"

for lab in labs:
    capture = re.compile(capture_string)
    s = capture.findall(lab)
    if s != []:
        score = testing_module_4.test(s[0][0], s[0][1], path = grade_path)
        data.append(score)
        print("Graded:", s[0][0], "\n")
    else:
        reject.append(lab)
        
if data:
    crw.setData(path = directory_path + score_path , title = "lab"+lab_number+"_scores", data = data)
    if reject:
        print("Files not graded", reject)
else:
    print("No labs were graded.")

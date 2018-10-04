#grading script lab3

#set grading paths
lab_number = "3"
grade_path = "/lab"+lab_number+"_to_grade/"
score_path = "/lab"+lab_number+"_scores/"

import re
import os
import crw
import testing_module_3
directory_path = os.path.dirname(os.path.realpath(__file__))

labs = os.listdir(directory_path + grade_path)
data = []
reject = []
capture_string ="((.*)_lab"+lab_number+").py"

for lab in labs:
    capture = re.compile(capture_string)
    s = capture.findall(lab)
    if s != []:
        score = testing_module_3.test(s[0][0], s[0][1], path = directory_path + grade_path + s[0][0]+ ".py")
        data.append(score)
        print("Graded:", s[0][0], "\n")
    else:
        reject.append(lab)
        
if data:
    crw.setData(path = directory_path + score_path , title = "lab3_scores", data = data)
    if reject:
        print("Files not graded", reject)
else:
    print("No labs were graded.")

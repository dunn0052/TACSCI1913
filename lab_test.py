#grading script lab1

import re
import os
import crw
import testing_module_2
directory_path = os.path.dirname(os.path.realpath(__file__))
grade_path = "/lab2_to_grade/"
score_path = "/lab2_scores/"
labs = os.listdir(directory_path + grade_path)
data = []
for lab in labs:
    capture = re.compile("((.*)_lab2).py")
    s = capture.findall(lab)
    if s != []:
        try:
            score = testing_module_2.test(s[0][0], s[0][1], path = directory_path + grade_path + s[0][0]+ ".py")
            data.append(score)
            print("Graded:", s[0][0], "\n")
        except:
            print("Couldn't process: check out", s[0][0], "\n")
crw.setData(path = directory_path + score_path , title = "lab2_scores", data = data)

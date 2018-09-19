#grading script lab1

import re
import os
import crw
import testing_module_2
path = "lab2_to_grade/"
labs = os.listdir(path)
data = []
for lab in labs:
    capture = re.compile("((.*)_lab2).py")
    s = capture.findall(lab)
    if s != []:
        try:
            score = testing_module_2.test(s[0][0], s[0][1], path = path + s[0][0]+ ".py")
            data.append(score)
            print("Graded:", s[0][0], "\n")
        except:
            print("Couldn't process: check out", s[0][0], "\n")
crw.setData(path = "/lab1_scores/", title = "lab1_scores", data = data)

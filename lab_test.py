#grading script lab1

import re
import os
import crw
import testing_module_1

labs = os.listdir()

for lab in labs:
    capture = re.compile("((.*)_lab1).py")
    s = capture.findall(lab)
    data = []
    if s != []:
        try:
            data.append(testing_module_1.test(s[0][0], s[0][1]))
            print("Graded:", s[0][0])
        except:
            print("Couldn't process: check out", s[0][0])
crw.setData("scores", data)
    

#grading script lab1

import re
import os
import crw
import testing_module_1

labs = os.listdir()

for lab in labs:
    capture = re.compile("((.*)_lab1).py")
    s = capture.findall(lab)
    if s != []:
        data = []
        print(s[0][0])
        try:
            testing_module_1.test(s[0][0], s[0][1])
        except:
            print("Bad module", s[0][0])
            
        #print(s[0][1])
        #setData(score, "scores")
    

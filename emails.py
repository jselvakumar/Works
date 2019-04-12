
import re 

emil = open("/Users/selvakumarjeremiah/email.txt", "r")
#print emil.readlines()
for emils in emil:
    regx = re.match(r'([\w\.-]+@[\w\.-]+)', emils) 
    if regx:
        print regx.group(1)
    else:
        continue 

    


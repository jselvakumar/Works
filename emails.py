
import re 

emil = open("/Users/selvakumarjeremiah/email.txt", "r")
#print emil.readlines()
for emils in emil:
    regx = re.findall(r'[\w\.-]+@[\w\.-]+', emils)
    for empty in regx:
        if empty!=[]:
           empty.strip()   
    print (empty)
    


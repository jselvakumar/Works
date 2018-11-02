#!/usr/bin/python

import os
import subprocess
from subprocess import Popen, PIPE
import shlex
import re
import sys
import json
import pprint
from jira import JIRA
jira = JIRA(basic_auth=('e5350756', 'Time2!@#123'), server='http://gfr4repsatlap01.kordoba.de:8090')
git_path="C:\\Program Files\\Git\\bin"
sys.path.append ("\\\\kunx0014\\migration\\python\\lib\\3.4\\site-packages")
os.environ["PATH"] += os.pathsep + git_path

#dest_path = "C:\\Users\\selvaj\\Assyst\\"
file = os.listdir("\\\\kunx0014\\compot\\Assyst_Auftraege\\XREF_S100\\5_prod\\s100-24\\")
struct = {}
for csv in file:
    f_path ="\\\\kunx0014\\compot\\Assyst_Auftraege\\XREF_S100\\5_prod\\s100-24\\" + csv
    csvopen = open(f_path, "r")
    #filename = f_path.split('/')
    #print (filename)
    #print("File:%s" % f_path)
    obj = re.search(r'(R\d+)-', csv)
    if (obj):
        assyst = (obj.group(1))
        #print(assyst)
        #print (len(assyst))
        if assyst not in struct:
            struct[assyst]=[]
		  
        	   
    for eachline in csvopen:
        #print("\t%s" % eachline);
        fields = eachline.split(';')
        xpname = fields[28]
        #print (xpname)
        filename = re.search(r'.*\/(.*)\@\@', xpname)
        searchinput =(filename.group(1))
        #print (searchinput)
        struct[assyst].append(searchinput)
        #json_out = json.dumps(struct)
jira_creation =(len(struct))
#print (jira_creation)
pprint.pprint(struct)
for key in struct.keys():
    summary = "XREF ticket -" + key
    issue_dict = {
    'project': {'key': 'KDBPOC'},
    'summary': summary,
    'parent' : {'key' : 'KDBPOC-967'},
    'issuetype': {'name': 'Sub-task'},
    'priority' : {'id' : '3'},
    #'customfield_10178' : {'value' : 'BANKCONTROL'},
    #'customfield_10176' : {'value' : 'ING KGS'},
    'customfield_10198' : {'value' : 'S100'}
    }
    new_issue = jira.create_issue(fields=issue_dict)
    jira.assign_issue(new_issue, 'e5350756')
    print(new_issue.key)
       
        
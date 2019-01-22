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
jira = JIRA(basic_auth=('selvakuj', 'xxxxxxxx'), server='http://xxxxx.xx:8090')
git_path="C:\\Program Files\\Git\\bin"
sys.path.append ("\\\\older\\migration\\python\\lib\\3.4\\site-packages")
os.environ["PATH"] += os.pathsep + git_path

file = os.listdir("\\\\older\\folder2\\")
struct = {}
for csv in file:
    f_path ="\\\\older\\folder2\\" + csv
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
    'project': {'key': 'JIRA_PAD'},
    'summary': summary,
    'parent' : {'key' : 'JIRA_PAD-967'},
    'issuetype': {'name': 'Sub-task'},
    'priority' : {'id' : '3'},
    #'customfield_10178' : {'value' : 'BCCCNKSK'},
    #'customfield_10176' : {'value' : 'INNN'},
    'customfield_10198' : {'value' : '23456789'}
    }
    new_issue = jira.create_issue(fields=issue_dict)
    jira.assign_issue(new_issue, 'username')
    print(new_issue.key)
       
        

import sys
sys.path.append ("\\\\kunx0014\\migration\\python\\lib\\3.4\\site-packages")
from jira import JIRA
jira = JIRA(basic_auth=('e5350756', 'Time2!@#123'), server='http://gfr4repsatlap01.kordoba.de:8090')

for i in range(1):        
    summary = "XREF ticket -" + str(i)
    issue_dict = {
    'project': {'key': 'KDBJAVA'},
    'summary': summary,
    'parent' : {'key' : 'KDBJAVA-29'},
    'issuetype': {'name': 'Sub-task'},
    'priority' : {'id' : '3'},
    #'customfield_10178' : {'value' : 'BANKCONTROL'},
    #'customfield_10176' : {'value' : 'ING KGS'},
    'customfield_10198' : {'value' : 'ecore000'}
    }
    new_issue = jira.create_issue(fields=issue_dict)
    jira.assign_issue(new_issue, 'e5350756')
    print(new_issue.key)
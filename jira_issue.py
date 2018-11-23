import sys
sys.path.append ("\\\\older\\migration\\python\\lib\\3.4\\site-packages")
from jira import JIRA
jira = JIRA(basic_auth=('selvakuj', 'xxxxx'), server='http://gxxxx.xx:8090')

for i in range(1):        
    summary = "XREF ticket -" + str(i)
    issue_dict = {
    'project': {'key': 'JIRA_JAVA'},
    'summary': summary,
    'parent' : {'key' : 'JIRA_JAVA-29'},
    'issuetype': {'name': 'Sub-task'},
    'priority' : {'id' : '3'},
    'customfield_10198' : {'value' : 'mandatory'}
    }
    new_issue = jira.create_issue(fields=issue_dict)
    jira.assign_issue(new_issue, 'selvakuj')
    print(new_issue.key)

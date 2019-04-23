
import requests
import json
import re
import pprint

url = "https://api.github.com/repos/jselvakumar/Works"

reqget = requests.get(url)

reqgetjson = reqget.json()

clone = reqgetjson["owner"]
ineed=['clone_url','created_at','updated_at','pushed_at']
for detail in ineed:
    if detail in reqgetjson:
#        print ("%s : %s"%(detail,reqgetjson[detail]))
         print (detail,":",reqgetjson[detail])
#pprint.pprint (clone)
pprint.pprint (clone)

#pprint.pprint (reqgetjson)



import requests
import json
import re
import pprint

url = "https://api.github.com/repos/jselvakumar/Works"

reqget = requests.get(url)

reqgetjson = reqget.json()

clone = reqgetjson["owner"]

pprint.pprint (clone)

#pprint.pprint (reqgetjson)


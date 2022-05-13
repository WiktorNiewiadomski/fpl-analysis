import requests


URL = "https://data.fantasyfootballhub.co.uk/api/players-attack"

PARAMS = {
    'mingw': 36,
    'maxgw': 36,
    'type': 'total',
    'venue': 'all',
    'season': 2021,
    'sortOn': 'points',
    'qty':100,
    'sortOrder': 'desc',
    'playerSearch': '',
    'minCost': 0,
    'maxCost': 135,
    'positions': '1,2,3,4',
    'min_fdr': 1,
    'max_fdr': 5,
    'page_No': 1,
    'lowMins': False,
    'ppm': 0

}

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvY21zLmZhbnRhc3lmb290YmFsbGh1Yi5jby51ayIsImlhdCI6MTY1MTk5NTA1NCwibmJmIjoxNjUxOTk1MDU0LCJleHAiOjE5NjczNTUwNTQsImRhdGEiOnsidXNlciI6eyJpZCI6IjUyNzk5In19fQ.fmqPn_wOuVykWwV1zk2xOBgiQoEriZlTUW4WqTQ0e2E'

HEADERS = {
    'Token': 'Bearer ' + TOKEN,
    'Authorization': 'r5C(e3.JeS^:_7LF'
}

response = requests.get(url = URL, params = PARAMS, headers = HEADERS)

data = response.json()

#print(data)

import json

json_formatted_str = json.dumps(data, indent=2)

print(json_formatted_str)
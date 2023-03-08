import requests
import json
response = requests.get("https://api.github.com/repos/rahulmrnaico/Technology/events")
data = response.text
parse_json = json.loads(data)
active_case = parse_json[0]['payload']['head']
# print(active_case)

import subprocess
# subprocess.run('git init')
# subprocess.run('git add .')
# subprocess.run(f'git commit -m "hi"')
# subprocess.run('git push')
# subprocess.run('python')
subprocess.run('git checkout '+ active_case)
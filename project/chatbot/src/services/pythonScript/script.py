import sys
import json
import json
import sys
import requests

url = 'localhost:4000/api/v1/category/b.17'
r = requests.get(url)
data = r.json()

print(json.dumps(data))
sys.stdout.flush()

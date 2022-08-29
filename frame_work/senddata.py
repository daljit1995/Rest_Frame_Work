import requests
import json

URL='http://127.0.0.1:8000/save'
data={'name':'Jaspreet','roll':'13','email':'ggarry484@gmail.com'}
data=json.dumps(data)
r=requests.post(url=URL,data=data)
data=r.json()
print(data)
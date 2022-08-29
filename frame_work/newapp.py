import requests
import json

URL='http://127.0.0.1:8000/newapp'

def getdata(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    # dump use for covert data in json
    # loads use for covert data in python native
    r=requests.get(url=URL,data=json_data)
    r=r.json()
    print(r)

def postdata():
    data={'name':'Jaspreet','roll':13,'email':'ggarry484@gmail.com'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    r=r.json()
    print(r)

getdata()

def updatedata():
    data={'id':1,'name':'Shubham','roll':15}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

updatedata()
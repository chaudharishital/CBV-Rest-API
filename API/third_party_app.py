import requests
import json


def post_data():
    dict1={
    "ename":'Shital',
    "esal":50000,
    "eaddress":"Karjat"
    }
    json_data=json.dumps(dict1)
    URL="http://127.0.0.1:8000/emp_insert/"
    req=requests.post(url=URL,data=json_data)
    res=req.json()
    print(res)
post_data()

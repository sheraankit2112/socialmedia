import requests
import json

data={"id":1}

json_data=json.dumps(data)

r=requests.delete("http://127.0.0.1:8000/delete/",data=json_data)
data=r.json()
print(data)
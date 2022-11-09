import requests
import json

data={"id":1,"name":"sahil","age":24}

json_data=json.dumps(data)

r=requests.put("http://127.0.0.1:3456/update",data=json_data)
data=r.json()
print(data)
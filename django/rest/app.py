import requests
import json
data={"id":1,"name":"sahilo","age":20}
headers={'content-Type':'application/json'}
json_data=json.dumps(data)
r=requests.put("http://127.0.0.1:3456/",headers=headers,data=json_data)
data=r.json()
print(data)
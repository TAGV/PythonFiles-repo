import json
import requests

my_json = json.load(open("file.json","r"))      # Json file converted to python dictionary
print(type(my_json))
print(dict(my_json).keys())
print(dict(my_json).values())
print(len(my_json))

for k,v in dict(my_json).items():
    print(k,"------------>",v)

#Serialize ``obj`` as a JSON formatted stream to ``fp``
conv = json.dump(my_json,open("myfile.json","w"),indent=4)  #Python dictionary converted back to json
print(type(conv))


print("===============================================================================")

req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
req_text = req.text

my_requests = json.loads(req_text)
print(type(my_requests))
print(len(my_requests))
print(dict(my_requests).keys())
print(dict(my_requests).values())

conv2json_str = json.dumps(my_requests,indent=3)    #Serialize ``obj`` to a JSON formatted ``str
print(type(conv2json_str))
print(conv2json_str)

bitcoin = json.dump(my_requests,open("btc.json",'w'),indent=3)
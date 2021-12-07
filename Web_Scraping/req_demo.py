import requests


res = requests.get("https://acloudguru.com/blog/tag/aws")

#print(type(res))
#print(dir(res))
#print(res)

#print(res.content)
#print(res.text)
#print(res.headers)
#print(res.status_code)
#print(res.content)

with open("testfile","w") as f:
    f.write(res.text)
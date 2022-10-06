import requests as req

header = {'User-agent':'ubuntu 36'}

try:
    req = req.get('https://putsreq.com/YerasvAxD0eaz8w2qaue?name=Geralt',
                  headers = header)
    print(req.text)
except Exception as err:
    print("Request error:" , err)
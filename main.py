import requests as rq


response = rq.get(url="http://api.open-notify.org/iss-now.json")
print(response)
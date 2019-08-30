from requests import Request, Session
import requests
from requests.auth import HTTPBasicAuth
import json
from django.middleware.csrf import get_token

#url = "http://localhost:8051/login_user/"
username = 'user1'
password = 'Pass4321'
url = "http://localhost:5001/auth_login/"
formdata = {'username':username, 'password':password}
#auth = HTTPBasicAuth(username, password)
#url = "http://localhost:8051/login_user/"
#client = requests.session()
# Retrieve the CSRF token first
#csrf = client.get(url).headers.get('name')
#print("ddd",csrf)


try:
    r = requests.post(url=url, data=formdata)
    #print("Return status -", r.status_code)
except:
    r.status_code
    #print("Return Error --", r.status_code)

if r:
    data = json.loads(r.text)
    print ("data received", type(data), data)
    #uid = data[requests.data]
    #print("---Returned Username as -- ", uid)
    print("session", )
else:
    print("Error", r.text)



"""
try:
    r = requests.post(url=url, data=data)
    print("return status ",r.status_code, r.text)
    #requests.sessions.Session.close()
except:
    r.status_code

if r:
    data = json.loads(r.text)
    print ("data received", type(data))
    uid = data['uid']
    print("---Returned Username as -- ", uid)
    print("session", )

del r.session
data = json.loads(r.text)
print ("data received", type(data))
uid = data['uid']
r.close()

print("---uid-", uid)

s = Session()
req = Request('POST', url=url, data=data, headers=headers, verify=False)
prepped = req.prepare()
resp = s.send(prepped)

if resp:
    print(resp.status_code)
    data = json.loads(resp.text)
    print("data received", type(data))
    uid = data['uid']
    print("---data--", data)

data = json.loads(resp.text)
print ("data received", type(data))
uid = data['uid']
print("--should -uid--",uid)

#requests.session.modified = True
url = "http://localhost:8051/logout_user/"
req = Request('POST', url=url)
prepped = req.prepare()
resp = s.send(prepped)

s.delete(url)
s.close()

print("---delete - uid--", uid, s.verify)
print("resp--",resp.text)
"""
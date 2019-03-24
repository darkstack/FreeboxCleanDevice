__author__ = 'Tom'
import json
import requests

print("Cleaning Device List")
print("Get the token with firefox in the params of a request")
token = input("token: ")
ip = 'mafreebox.free.fr'
token = 'FREEBOXOS="'+token+'"'
print("Auth")
requestList = 'http://' + ip + '/api/v6/lan/browser/pub/'

r = requests.get(requestList, headers={'Cookie': token})
print(r.status_code)
json = r.json()
for t in json['result']:
    print('Delete ' + t['primary_name'])
    requestDelete = 'http://' + ip + '/api/v6/lan/browser/pub/'+t['id']
    print(requestDelete)
    requests.delete(requestDelete, headers={'Cookie': token},params=t)

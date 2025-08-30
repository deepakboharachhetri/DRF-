import requests
endpoint="http://localhost:8000/api/products/"
sent_request=requests.get(endpoint,params={"title":123,"score":"heroic"},json={"title ":"title1"})
print(sent_request.text)
import requests 
endpoint="http://localhost:8000/api/products/create/"
get_response=requests.post(endpoint,json={"title":"first title create api view","price":123})
print(get_response.text)
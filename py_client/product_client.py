import requests
# endpoint="http://localhost:8000/api/product/"
endpoint="http://localhost:8000/api/"
# get_response=requests.get(endpoint,params={"product_id":1},json={"messages":"hello world"})
get_response=requests.post(endpoint,json={"title":"hello world"})

print(get_response.json())
print(get_response.status_code)
import requests 
# getting view
endpoint="http://localhost:8000/api/products/create_list/"
# creating a new product
endpoint="http://localhost:8000/api/products/create_list/"
get_response=requests.post(endpoint,json={"title":"vaiyaji","price":"211","content":"hello my name is content"})
print(get_response.text)
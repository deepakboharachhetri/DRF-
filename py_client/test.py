import requests 
endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
get_response=requests.get(endpoint,json={"query":"hello world "})        #API Method
print(get_response.text) # print raw text  

# client through python 

# Http request -> HTML
# REST API HTTP request -> JSON(javascript object notation)~ dcict 

# json function have two types .load() is used  to covert json into python object for dumps() for viceversa and json () for both 
print(get_response.json())

print (get_response.status_code)
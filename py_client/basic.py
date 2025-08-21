import requests 
endpoint = " http://127.0.0.1:8000/api/"#http://localhost:8000/
get_response=requests.get(endpoint,params={"abc":123},json={"querry":"hello world"})        #API Method
#params is used for the paramete for example http://localhost:8000/api/?abc=123
# request->httprequest->django 
print(get_response.json())

print (get_response.status_code)
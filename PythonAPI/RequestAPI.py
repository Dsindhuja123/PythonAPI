import requests
import random
import json
import string

base_url = "https://gorest.co.in"

auth_token = "Bearer 942e1ac05dc41ac46c791c956e12d8b756fec27968391c6ab4c2d18923f26d6d"
              

def get_request():
    url = base_url + "/public/v2/users"
    print("get url: " + url)
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: " , json_str)

'''
def post_request():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    headers = {"Authorization" : auth_token}
    data = {
        "name": "Neha",
        "email": "neha1@lebsack.test",
        "gender": "female",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    user_id = json_data["id"]
    assert "name" in json_data 
    assert json_data["name"] == "Neha"
    return user_id


def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "def update",
        "email": "defupdated@lebsack.test",
        "gender": "female",
        "status": "inactive"  
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "def"  '''




def post_request():
    base_url = "https://gorest.co.in"
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    auth_token = "Bearer 942e1ac05dc41ac46c791c956e12d8b756fec27968391c6ab4c2d18923f26d6d"  # Replace with your actual auth token
    headers = {"Authorization": auth_token}
    data = {
        "name": "qwe",
        "email": "qwe777533@gmail.com",
        "gender": "female",
        "status": "inactive"
    }
    response = requests.post(url, json=data, headers=headers)
    print("Response status code:", response.status_code)
    
    if response.status_code == 201:
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("json POST response body: ", json_str)
        user_id = json_data["id"]  # Access user ID directly from the root level
        if "name" in json_data and json_data["name"] == "qwe":
            print("User created successfully with ID:", user_id)
            return user_id
        else:
            print("Error: Name in response does not match expected name.")
            return None
    else:
        print("Error:", response.text)
        return None
 
def put_request(user_id):
    if user_id is None:
        print("User ID is None. Cannot make PUT request.")
        return
    
    base_url = "https://gorest.co.in"
    url = base_url + f"/public/v2/users/{user_id}"
    print("put url: " + url)
    auth_token = "Bearer 942e1ac05dc41ac46c791c956e12d8b756fec27968391c6ab4c2d18923f26d6d"  # Replace with your actual auth token
    headers = {"Authorization": auth_token}
    data = {
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    print("Response status code:", response.status_code)
    
    if response.status_code == 200:
        print("User updated successfully.")
    else:
        print("Error:", response.text)
 
user_id = post_request()
if user_id:
    put_request(user_id)
else:
    print("User creation failed.")



def delete_request(user_id):
    if user_id is None:
        #print("User ID is None. Cannot make DELETE request.")
        return
    
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        print("Deleted Successfully....")
        print("Get user is done....")
        print("=======....")
    else:
        print("Error:", response.text)



'''def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    headers = {"Authorization": auth_token}
    reponse = requests.delete(url, headers=headers)
    assert reponse.status_code == 204
    print("Deleted Successfully....")
    print("Get user is done....")
    print("=======....")'''


    


#get_request()   
user_id = post_request()
#put_request(user_id)
delete_request(user_id)

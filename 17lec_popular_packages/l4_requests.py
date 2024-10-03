import requests

# url = "https://jsonplaceholder.typicode.com/users"
# r = requests.get(url, timeout=10)
# print(
# r.status_code,
# r.text,
# )
# users = r.json() if not r.json() is None else []
# for user in users:
#     print(user["name"])

# # url = "https://jsonplaceholder.typicode.com/users/1"
# # r = requests.get(url, timeout=10)
# # user = r.json() if not r.json() is None else {}
# # name = user.get("name", "")
# print(name)

# url = "https://jsonplaceholder.typicode.com/users"
# user_req = {
#     "id": 11,
#     "name": "Chanchito Feliz",
# }
# r = requests.post(url, timeout=10, data=user_req)
# print(r.status_code, r.json())

# url = "https://jsonplaceholder.typicode.com/users/2"
# user_req = {
#     "name": "Chanchito Feliz",
# }
# r = requests.put(url, timeout=10, data=user_req)
# print(r.status_code, r.json())

url = "https://jsonplaceholder.typicode.com/users/2"
api_key = "1234546"
headers = {
    "Authorization": f"Bearer {api_key}",
}
r = requests.delete(url, timeout=10, headers=headers)
print(r.status_code)

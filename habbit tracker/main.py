import requests
from datetime import datetime

ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "j3hba69swg2rrkq1v"
USERNAME = "kumi"
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

profile_page = " https://pixe.la/@kumi"
# response = requests.post(url = ENDPOINT, json= params)
# print(response.text)


graph_endpoint = f"{ENDPOINT}/{USERNAME}/graphs"
ID = "graph1"

graphs_params = {
    "id": ID,
    "name": "Reading Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graphs_params, headers = headers)
# print(response.text)
 
post_endpoint = f"{graph_endpoint}/{ID}"

today = datetime(year=2023, month=8, day=1)
print(today.strftime("%Y%m%d"))

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50.32"
}

# response = requests.post(url = post_endpoint, json=post_params, headers = headers)
# print(response.text)


update_pixel_endpoint = f"{post_endpoint}/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity": "30",
}

# response = requests.put(url=update_pixel_endpoint, json=update_params, headers = headers)
# print(response.text)

delete_pixel_endpoint = f"{post_endpoint}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint, headers = headers)
print(response.text)
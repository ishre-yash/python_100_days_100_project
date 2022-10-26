from ast import If
import requests
from datetime import datetime

# "https://pixe.la/@ishreyash"

USERNAME = "ishreyash"
TOKEN = "iamshreyash7777"
GRAPH_ID = "ishreyash1"

pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.now()

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "h",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
user = int(input(
    f"Habit Tracker {today} :\n  1 for Todays Data\n  2 for Updating Data\n  3 for DELETE\n\t"))

if user == 1:
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("How many hours did you code today?"),
    }
    response = requests.post(url=pixel_creation_endpoint,
                             json=pixel_data, headers=headers)
    print(response.text)

elif user == 2:
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    new_pixel_data = {
        "quantity": input("Updating...\n How many hours did you code today?")
    }

    # PUT
    response = requests.put(url=update_endpoint,
                            json=new_pixel_data, headers=headers)
    print(response.text)

elif user == 3:
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    # DELETE
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)

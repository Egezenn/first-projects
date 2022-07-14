import requests
from datetime import datetime

now = str(datetime.now()).split(" ")[0].split("-")  # now.strftime("<pass in format codes>") # use timedelta for edit
date = "".join(now)

TOKEN = ""
USERNAME = ""
GRAPH_ID = ""
GRAPH_NAME = ""

header = {
    "X-USER-TOKEN": TOKEN
}

# pixela_endpoint = "https://pixe.la/v1/users"
#
# user_paramaters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": GRAPH_NAME,
#     "unit": "commit",
#     "type": "int",
#     "color": "kuro"
# }

# body = {
#     "date": date,
#     "quantity": "1",
# }
#
# graph_post = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
#
# response = requests.post(url=graph_post, json=body, headers=header)
# response.raise_for_status()

graph_edit = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date}"

body = {
    "date": date,
    "quantity": "0",
}

response = requests.put(url=graph_edit, json=body, headers=header)
response.raise_for_status()

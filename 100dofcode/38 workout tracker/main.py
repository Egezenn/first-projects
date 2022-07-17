import requests
import pytz
#  import json
from datetime import datetime

uinp = str(input("Please enter what you've done today!\n"))

#  todo export & os.environ.get()
APP_ID = ""
API_KEY = ""
GENDER = ""
WEIGHT = 0
HEIGHT = 0
AGE = 0
TIMEZONE = ""

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
parameters = {
    "query": uinp,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}

post = requests.post(url=url, json=parameters, headers=headers)
post.raise_for_status()
post_response = post.json()

timezone = pytz.timezone(TIMEZONE)
nowdate = datetime.now(tz=timezone).strftime("%d/%m/%Y")
nowtime = datetime.now(tz=timezone).strftime("%H:%M:%S")

#  if csv file is not existent it creates one with a template, else ignores.
try:
    with open("workout.csv") as file:
        print("File found!")

except FileNotFoundError:
    with open("workout.csv", mode="w") as file:
        print("File not found, creating file!")
        file.write("Date,Time,Exercise,Duration,Calories\n")

#  write exercise(s) data to a csv file and print what the data is.
for exercise in post_response["exercises"]:
    duration = exercise["duration_min"]
    name = exercise["name"]
    calories = exercise["nf_calories"]

    with open("workout.csv", mode="a") as file:
        file.write(f"{nowdate},{nowtime},{name},{duration},{calories}\n")

    print(f"On {nowdate} {nowtime}, you've done '{name}' for {duration}mins and burnt {calories}cal!")


# with open("dump.json", mode="w") as file:
#     json.dump(post_response, file, indent=4)

#  i don't think i like apis

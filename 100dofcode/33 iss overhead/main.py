import requests
import datetime
from time import sleep
# from tkinter import *

TARGET_LAT = 0 # change
TARGET_LON = 0 # change
TIMEZONE = 0  # change

parameters = {
    "lat": TARGET_LAT,
    "lon": TARGET_LON,
    "formatted": 0
}


def lat_lon_check(latitude, longitude, target_lat, target_lon):
    """checks if the latitude and longitude is in the range of target latitude and target longitude"""

    if target_lat + 5 >= latitude >= target_lat - 5:

        if target_lon + 5 >= longitude >= target_lon - 5:
            return True

        else:
            return False

    else:
        return False


def nighttime_check(current_hour, sunrise_time, sunset_time, timezone):
    """checks if it is nighttime, timezone is required due to sunrise-sunset api giving time in the default timezone"""

    if current_hour - timezone <= sunrise_time:

        if current_hour - timezone >= sunset_time:
            return True

        else:
            return False

    else:
        return False


while True:
    # current time
    now = datetime.datetime.now()

    # get lat & lon of iss
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    lat = float(response.json()["iss_position"]["latitude"])
    lon = float(response.json()["iss_position"]["longitude"])
    response.raise_for_status()

    # get sunrise & sunset hours
    request = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    request.raise_for_status()
    sunrise = int(request.json()["results"]["sunrise"].split("T")[1].split("+")[0].split(":")[0])
    sunset = int(request.json()["results"]["sunset"].split("T")[1].split("+")[0].split(":")[0])

    if lat_lon_check(lat, lon, TARGET_LAT, TARGET_LON):

        if nighttime_check(now.hour, sunrise, sunset, TIMEZONE):
            print("look up!")  # wonder if there is a pollution api

        else:
            print(f"lat&lon does match! however it is currently daytime. time: {now.hour},"
                  f" nighttime: before {sunrise} and after {sunset}")

    else:
        print(f"lat&lon doesn't match! lat: {lat} / lon: {lon}")

    sleep(30)


# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     canvas.itemconfigure(quote_text, text=response.json()["quote"])
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 24, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()

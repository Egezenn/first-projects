import smtplib
import ssl
import requests
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def days_in_month(year, month):
    if is_leap(year):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return month_days[month-1]


paramaters = {
    "lat": 0,  # todo change
    "lon": 0,  # todo change
    "units": "metric",
    "exclude": "current,minutely,daily",
    "appid": "0"  # todo change os.environ.get("OWM_API_KEY")
}

url = "https://api.openweathermap.org/data/2.5/onecall"
weather_data = requests.get(url=url, params=paramaters)
weather_data.raise_for_status()
json_weather_data = weather_data.json()

next_12_hours = json_weather_data["hourly"][:12]
will_rain = False

current_date = datetime.now()
time_zone = 0  # system time zone  # todo change
mail_str = ""
date = f"{current_date.day}/{current_date.month}/{current_date.year}"

for hour in next_12_hours:

    time = int(current_date.hour - time_zone + next_12_hours.index(hour) + json_weather_data["timezone_offset"] / 3600)

    if time >= 24:
        time %= 24

        if len(str(time)) == 1:
            time = f"0{time}.00"

        else:
            time = f"{time}.00"

        days_in_current_month = days_in_month(current_date.year, current_date.month)

        if days_in_current_month >= current_date.day:
            date = f"{current_date.day + 1}/{current_date.month}/{current_date.year} "

        else:
            if current_date.month <= 12:
                date = f"1/{current_date.month + 1}/{current_date.year} "
            else:
                date = f"1/1/{current_date.year + 1} "

    if hour["weather"][0]["id"] < 800:
        mail_str += f'{date}{time}: {hour["weather"][0]["description"].title()}<br>'
        will_rain = True

    else:
        mail_str += f'{date}{time}: {hour["weather"][0]["description"].title()}<br>'


if will_rain:
    smtp_server = ""  # todo change os.environ.get("SMTP_SERVER")
    port = 0  # todo change os.environ.get("SMTP_PORT")
    sender_email = ""  # todo change os.environ.get("SENDER_EMAIL")
    password = ""  # todo change  os.environ.get("SENDER_PASSWORD")
    receiver_email = ""  # todo change os.environ.get("RECEIVER_EMAIL")

    message = MIMEMultipart("alternative")
    message["Subject"] = "WEATHER REMINDER"
    message["From"] = sender_email
    message["To"] = receiver_email

    # i don't know why but the text gets quoted randomly
    html = f"""\
    <html>
      <body>
        <p>In the next 12 hours it's going to rain!<br>
            {date}<br><br>
            {mail_str}<br>
        </p>
      </body>
    </html>
    """
    html = MIMEText(html, "html")
    message.attach(html)

    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

    except Exception as e:
        print(e)

else:
    print("No rain")

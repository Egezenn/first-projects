import requests
import json
import pytz
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# variables for mail todo os.environ.get() export
smtp_server = ""
port = 0
sender_email = ""
password = ""
receiver_email = ""

# variables for stock api todo os.environ.get() export
STOCK = "TSLA"
FUNCTION = "TIME_SERIES_DAILY"
API_KEY_STOCK = ""

# variables for news api todo os.environ.get() export
COMPANY_NAME = "Tesla%20Inc"
API_KEY_NEWS = ""

# variables for time
TIME_ZONE = pytz.timezone("US/Eastern")
current_date_list = str(datetime.now(tz=TIME_ZONE)).split(" ")[0].split("-")
one_day_ago_list = str(datetime.now(tz=TIME_ZONE) - timedelta(days=1)).split(" ")[0].split("-")  # wish i knew
two_days_ago_list = str(datetime.now(tz=TIME_ZONE) - timedelta(days=2)).split(" ")[0].split("-")  # tz&timedelta yesterday
today = "-".join(current_date_list)
one_day_ago = "-".join(one_day_ago_list)
two_days_ago = "-".join(two_days_ago_list)

urlStock = f"https://www.alphavantage.co/query?function={FUNCTION}&symbol={STOCK}&apikey={API_KEY_STOCK}"
json_requestStock = requests.get(url=urlStock).json()

urlNews = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={two_days_ago}&to={today}&sortBy=relevancy&apiKey={API_KEY_NEWS}"
json_requestNews = requests.get(url=urlNews).json()


def mail(stockjson, newsjson, var_smtp_server, var_port, var_sender_email, var_password, var_receiver_email):  # are all these paramaters required?
    message = MIMEMultipart("alternative")
    message["Subject"] = "STOCK UPDATE"
    message["From"] = var_sender_email
    message["To"] = var_receiver_email

    one_day_ago_closing = float(stockjson["Time Series (Daily)"][one_day_ago]["4. close"])
    two_days_ago_closing = float(stockjson["Time Series (Daily)"][two_days_ago]["4. close"])

    news = f"""
    {newsjson["articles"][0]["title"]}<br><br>
    {newsjson["articles"][0]["url"]}<br>
    description: {newsjson["articles"][0]["description"]}<br><br><br><br>
    
    {newsjson["articles"][1]["title"]}<br><br>
    {newsjson["articles"][1]["url"]}<br>
    description: {newsjson["articles"][1]["description"]}<br><br><br><br>
    
    {newsjson["articles"][2]["title"]}<br><br>
    {newsjson["articles"][2]["url"]}<br>
    description: {newsjson["articles"][2]["description"]}"""

    if two_days_ago_closing + 2 >= one_day_ago_closing >= two_days_ago_closing - 2:
        html = f"""\
                <html>
                  <body>
                    <p>YOUR STOCK STAYED RELATIVELY THE SAME<br><br>
                    CURRENT: ${round(one_day_ago_closing, 2)}<br><br><br>
                    NEWS:<br><br>
                        {news}
                    </p>
                  </body>
                </html>
                """

    elif one_day_ago_closing < two_days_ago_closing:
        html = f"""\
        <html>
          <body>
            <p>YOUR STOCK WENT DOWN<br><br>
            BY: ${round(one_day_ago_closing - two_days_ago_closing, 2)}<br>
            CURRENT: ${round(one_day_ago_closing, 2)}<br><br><br>
            NEWS:<br><br>
                {news}
            </p>
          </body>
        </html>
        """

    else:
        html = f"""\
                <html>
                  <body>
                    <p>YOUR STOCK WENT UP<br><br>
                    BY: ${round(one_day_ago_closing - two_days_ago_closing, 2)}<br>
                    CURRENT: ${round(one_day_ago_closing, 2)}<br><br><br>
                    NEWS:<br><br>
                        {news}
                    </p>
                  </body>
                </html>
                """
    html = MIMEText(html, "html")
    message.attach(html)

    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(var_smtp_server, var_port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(var_sender_email, var_password)
        server.sendmail(var_sender_email, var_receiver_email, message.as_string())
        server.quit()

    except Exception as exception:
        print(exception)


mail(json_requestStock, json_requestNews, smtp_server, port, sender_email, password, receiver_email)

# data dumps
with open("stockDump.json", mode="w") as default:
    json.dump(json_requestStock, default, indent=4)
with open("newsDump.json", mode="w") as default:
    json.dump(json_requestNews, default, indent=4)

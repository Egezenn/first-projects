import requests

question_data = requests.get(url="https://opentdb.com/api.php?amount=20&type=boolean").json()

import requests


def history_requests():
    url = "https://api.spacexdata.com/v3/history"
    request = requests.get(url)
    data = request.json()

    for history in range(len(data)):
        print(
            f"• Title : {data[history]['title']}\n",
            f"• ID : {data[history]['id']}\n",
            f"• Event date UTC : {data[history]['event_date_utc']}\n",
            f"• Event date UNIX : {data[history]['event_date_unix']}\n",
            f"• Flight Number : {data[history]['flight_number']}\n",
            f"• Reddit : {data[history]['links']['reddit']}\n",
            f"• Article : {data[history]['links']['article']}\n",
            f"• Wikipedia : {data[history]['links']['wikipedia']}\n",
            f"• Details : {data[history]['details']}\n"
        )

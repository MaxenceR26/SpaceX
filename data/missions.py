import requests


def missions_requests():
    url = "https://api.spacexdata.com/v3/missions"
    request = requests.get(url)
    data = request.json()
    counter = 0
    for missions in range(len(data)):
        counter += 1
        if counter > 2:
            input("Continue...")
            counter = 0
        print(
            f"• Mission Name : {data[missions]['mission_name']}\n",
            f"• ID : {data[missions]['mission_id']}\n",
            f"• Wikipedia : {data[missions]['wikipedia']}\n",
            f"• Website : {data[missions]['website']}\n",
            f"• Twitter : {data[missions]['twitter']}\n",
            f"• Description : {data[missions]['description']}\n"
        )

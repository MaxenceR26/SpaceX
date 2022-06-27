import requests


def rockets_requests():
    url = "https://api.spacexdata.com/v3/rockets"
    request = requests.get(url)
    data = request.json()

    counter = 0
    for rockets in range(len(data)):
        counter += 1
        if counter > 2:
            input("Continue...")
            counter = 0
        print(
            f"• Name : {data[rockets]['rocket_name']}\n",
            f"• ID : {data[rockets]['id']}\n",
            f"• Active : {data[rockets]['active']}\n",
            f"• Stage : {data[rockets]['stages']}\n",
            f"• First Flight : {data[rockets]['first_flight']}\n",
            f"• Country : {data[rockets]['country']}\n",
            f"• Company : {data[rockets]['company']}\n",
            f"• Propellant-1 : {data[rockets]['engines']['propellant_1']}\n",
            f"• Propellant-2 : {data[rockets]['engines']['propellant_2']}\n",
            f"• Description : {data[rockets]['description']}\n"
        )

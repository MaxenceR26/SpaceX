import requests


def ships_requests():
    url = "https://api.spacexdata.com/v3/ships"
    request = requests.get(url)
    data = request.json()

    counter = 0
    for ships in range(len(data)):
        counter += 1
        if counter > 2:
            input("Continue...")
            counter = 0
        print(
            f"Ship name : {data[ships]['ship_name']} -> \n",
            f"• ID : {data[ships]['ship_id']}\n",
            f"• Roles : {data[ships]['roles'][0]}\n",
            f"• Imo : {data[ships]['imo']}\n",
            f"• Mmsi : {data[ships]['mmsi']}\n",
            f"• Abs : {data[ships]['abs']}\n",
            f"• Class : {data[ships]['class']}\n",
            f"• Weight lbs : {data[ships]['weight_lbs']}\n",
            f"• Weight kg : {data[ships]['weight_kg']}\n",
            f"• Year built : {data[ships]['year_built']}\n",
            f"• Home port : {data[ships]['home_port']}\n",
        )

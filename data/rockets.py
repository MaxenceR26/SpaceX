import requests


def rockets_requests():
    url = "https://api.spacexdata.com/v3/ships"
    request = requests.get(url)
    data = request.json()

    for rockets in range(len(data)):
        print(
            f"Ship name : {data[rockets]['ship_name']} -> \n",
            f"• ID : {data[rockets]['ship_id']}\n",
            f"• Roles : {data[rockets]['roles'][0]}\n",
            f"• Imo : {data[rockets]['imo']}\n",
            f"• Mmsi : {data[rockets]['mmsi']}\n",
            f"• Abs : {data[rockets]['abs']}\n",
            f"• Class : {data[rockets]['class']}\n",
            f"• Weight lbs : {data[rockets]['weight_lbs']}\n",
            f"• Weight kg : {data[rockets]['weight_kg']}\n",
            f"• Year built : {data[rockets]['year_built']}\n",
            f"• Home port : {data[rockets]['home_port']}\n",
        )

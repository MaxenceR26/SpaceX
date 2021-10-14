import requests


def info_spacex():
    url = "https://api.spacexdata.com/v3/info"
    request = requests.get(url)
    data = request.json()

    print(
        "SpaceX Info ->\n"
        f"• Founder : {data['founder']}\n"
        f"• Founded : {data['founded']}\n"
        f"• Employees : {data['employees']}\n"
        f"• Vehicles : {data['vehicles']}\n"
        f"• Launch Sites : {data['launch_sites']}\n"
        f"• Ceo : {data['ceo']}\n"
        f"• Cto : {data['cto']}\n"
        f"• Coo : {data['coo']}\n"
        f"• Cto Propulsion : {data['cto_propulsion']}\n"
        f"• Address : {data['headquarters']['address']}\n"
        f"• City : {data['headquarters']['city']}\n"
        f"• State : {data['headquarters']['state']}\n\n"
        f"• Summary : {data['summary']}\n"
    )

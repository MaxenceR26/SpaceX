import requests


def landspad_requests():
    url = "https://api.spacexdata.com/v3/landpads"
    request = requests.get(url)
    data = request.json()

    for pad in range(len(data)):
        print(
            f"• Full Name : {data[pad]['full_name']}\n",
            f"• ID : {data[pad]['id']}\n",
            f"• Location Name : {data[pad]['location']['name']}\n",
            f"• Location Region: {data[pad]['location']['region']}\n",
            f"• Landing Type : {data[pad]['landing_type']}\n",
            f"• Details : {data[pad]['details']}\n"
        )
